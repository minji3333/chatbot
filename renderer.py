import pandas as pd
import altair as alt
import streamlit as st
from utils import generate_short_id
from css import BUTTON_CSS, PRODUCTS_CSS

class ChatbotRenderer:
    def __init__(self, session, api_client):
        self.session = session
        self.api_client = api_client

    def render_main_categories(self):
        main_categories = self.api_client.get_main_categories()
        columns = st.columns(len(main_categories))
        for i, main_category in enumerate(main_categories):
            with columns[i]:
                st.button(main_category["name"], on_click=self.select_main_category, args=(main_category,))

    def select_main_category(self, main_category):
        self.session.set_state("selected_main_category", main_category)
        self.session.add_message("user", main_category["name"])
        self.session.add_message("assistant", f"{main_category['name']}을 찾으시는군요! 어떤 제품을 찾으시나요?")

    def render_sub_categories(self):
        selected_main_category = self.session.get_state("selected_main_category")
        sub_categories = self.api_client.get_sub_categories(selected_main_category["id"])
        columns = st.columns(len(sub_categories))
        for i, sub_category in enumerate(sub_categories):
            with columns[i]:
                st.button(sub_category["name"], on_click=self.select_sub_category, args=(sub_category,))

    def select_sub_category(self, sub_category):
        self.session.set_state("selected_sub_category", sub_category)
        self.session.add_message("user", sub_category["name"])
        self.session.add_message("assistant", "원하는 조건을 입력해주세요!")

    def render_conditions_input(self):
        if not self.session.get_state("conditions_submitted"):
            unique_key = f"current_input_{generate_short_id()}"
            st.chat_input("조건을 입력해주세요..", key=unique_key, on_submit=self.submit_conditions, args=(unique_key,))
        
    def submit_conditions(self, unique_key):
        conditions = self.session.get_state(unique_key)
        selected_sub_category = self.session.get_state("selected_sub_category")

        results = self.api_client.get_recommended_products(selected_sub_category["id"], conditions)

        self.session.set_state("conditions", conditions)
        self.session.add_message("user", conditions)

        if not results["products"]:
            self.session.add_message("assistant", f"조건에 일치하는 제품이 없습니다. 조건을 다시 입력해주세요!")
        else:
            aspects = ", ".join([f"{key}: {value}" for key, value in results["aspects"].items()])
            self.session.set_state("results", results)
            self.session.set_state("conditions_submitted", True)
            self.session.add_message("assistant", f"{aspects} 기준으로 추천된 제품입니다.\n\n마음에 드는 제품이 없다면 조건을 다시 입력해주세요!", callback=self.render_recommended_products)

    def render_recommended_products(self):
        st.markdown(PRODUCTS_CSS, unsafe_allow_html=True)

        results = self.session.get_state("results")

        if not results:
            return
        
        columns = st.columns(len(results["products"]))
        for i, recommended in enumerate(results["products"]):
            with columns[i]:
                product = recommended['product']
                with st.expander(label=f"**{i + 1}. {product['name']}**", expanded=True):
                    aspect_ratio = self.api_client.get_aspect_ratio(product["id"])
                    st.image("https://img.hankyung.com/photo/202406/01.36942977.1.jpg")
                    st.text(f"출시가격: {product['price']:,}원")
                    st.text(f"제조사: {product['manufacturer']}({product['release_year']})")
                    st.text(f"에너지 효율: {product['energy_efficiency']} ({product['power_consumption']}W)")
                    self.render_aspect_chart(aspect_ratio["aspect_ratios"])
                    st.button("최저가 구매하기", key=f"buy_{i}_{generate_short_id()}", on_click=self.select_product, args=(product,))
        
        if self.session.get_state("conditions_submitted"):
            col1, col2 = st.columns(2)
            with col1:
                st.button("처음으로", key=f"restart_{generate_short_id()}", on_click=self.reset_to_start)
            with col2:
                st.button("다시 입력", key=f"reset_{generate_short_id()}", on_click=self.reset_conditions)

    def render_aspect_chart(self, data):
        chart_data = pd.DataFrame({
            "aspects": [item["aspect"] for item in data],
            "positive": [float(item["positive_ratio"]) for item in data],
            "negative": [float(item["negative_ratio"]) for item in data]
        })
        
        # st.bar_chart(data, x="aspects", y=["positive", "negative"], color=["#FFABAB", "#83C9FF"], x_label="", y_label="", horizontal=True)

        # Altair 차트 생성
        bar_chart = alt.Chart(chart_data).transform_fold(
            fold=["positive", "negative"],  # 긍정/부정 열을 변환
            as_=["type", "value"]
        ).mark_bar().encode(
            y=alt.Y("aspects:N", title=None),
            x=alt.X("value:Q", title=None, axis=alt.Axis(labels=False, ticks=False)),
            color=alt.Color("type:N", scale=alt.Scale(domain=["positive", "negative"], range=["#83C9FF", "#FFABAB"]), legend=None),
            tooltip=["aspects:N", "type:N", "value:Q"]
        )

        # 막대 위에 값 표시
        text_chart = bar_chart.mark_text(
            align='center',  # 텍스트 정렬
            baseline='middle',  # 텍스트 위치
            dx=0  # 텍스트 막대와의 간격
        ).encode(
            y=alt.Y("aspects:N", title=None),  # y축 레이블 제거
            x=alt.X("value:Q"),  # x축 값
            text=alt.Text("value:Q", format=".1f"),  # 값 표시 (소수점 한 자리)
            color=alt.condition(
                "datum.type === 'positive'",  # 긍정/부정 색상 지정
                alt.value("white"),
                alt.value("white")
            )
        )
        
        chart = (bar_chart + text_chart).properties(
            height=250,
            title={
                "text": "주요 키워드별 분석",
                "anchor": "start",
                "fontSize": 16,  # 제목 글씨 크기
                "font": "sans-serif",
            }
        )

        # Streamlit에 렌더링
        st.altair_chart(chart, theme="streamlit", use_container_width=True)
        
    def select_product(self, product):
        search_url = f"https://search.shopping.naver.com/search/all?bt=-1&frm=NVSCPRO&query={product['name']}"
        js_code = f"""
        <script>
            window.open("{search_url}", "_blank");
        </script>
        """
        st.components.v1.html(js_code)

    def reset_to_start(self):
        st.markdown(BUTTON_CSS, unsafe_allow_html=True)
        self.session.set_state("selected_main_category", None)
        self.session.set_state("selected_sub_category", None)
        self.session.set_state("conditions", None)
        self.session.set_state("results", None)
        self.session.set_state("conditions_submitted", False)
        self.session.add_message("assistant", "처음으로 돌아갔습니다! 다시 시작해보세요.\n\n어떤 가전제품을 찾고 계신가요? 😊")
        
    def reset_conditions(self):
        self.session.set_state("conditions", None)
        self.session.set_state("conditions_submitted", False)
        self.session.add_message("assistant", "조건을 다시 입력해주세요!")