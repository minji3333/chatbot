import streamlit as st
from streamlit_chat import message
from utils.utils import load_css
from api.api_client import APIClient
from session.session import ChatbotSession
from ui.renderer import ChatbotRenderer

class ChatbotUI:
    def __init__(self):
        self.session = ChatbotSession()
        self.api_client = APIClient()
        self.renderer = ChatbotRenderer(self.session, self.api_client)

    def render_chat_ui(self):
        # 기존 메세지 표시
        for i, msg in enumerate(self.session.get_state("messages")):
            # <메세지 출력 방법>
            # 1. default, reloading 버벅임 없음
            # with st.chat_message(msg["role"]):
                # st.write(msg["content"])
            # 2. stream-chat, reloading 버벅임
            message(msg["content"], is_user=(msg["role"] == "user"), key=f"message_{i}")
            if "callback" in msg and msg["callback"]:
                msg["callback"]()
        
        # 상태에 따라 다른 UI 요소 표시
        if not self.session.get_state("selected_main_category"):
            self.renderer.render_main_categories()
        elif not self.session.get_state("selected_sub_category"):
            self.renderer.render_sub_categories()
        elif self.session.get_state("custom_sub_category") and not self.session.get_state("sub_category_input"):
            self.renderer.render_sub_category_input()
        elif not self.session.get_state("conditions") or not self.session.get_state("selected_product"):
            self.renderer.render_conditions_input()

        if self.session.get_state("show_restart_button"):
            self.renderer.render_restart_reset_button()

    def run(self):
        css_content = load_css("./src/ui/styles.css")
        st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="wide")
        st.title("🤖 Chatbot")
        st.caption("💬 Review-Based Home Appliance Recommendation Chatbot")
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
        self.render_chat_ui()


if __name__ == "__main__":
    if "ui" not in st.session_state:
        st.session_state["ui"] = ChatbotUI()
    
    st.session_state["ui"].run()