import streamlit as st

class ChatbotSession:
    def __init__(self):
        self.set_state("messages", [
            {"role": "assistant", "content": "안녕하세요. 사용자 리뷰 기반으로 가전제품을 추천해드리는 챗봇 \"CHATBOT\" 입니다.\n\n어떤 가전제품을 찾고 계신가요? 😊"}
        ])
        self.reset()

    def reset(self):
        self.set_state("selected_main_category", None)
        self.set_state("selected_sub_category", None)
        self.set_state("custom_sub_category", False)
        self.set_state("sub_category_input", None)
        self.set_state("conditions", None)
        self.set_state("conditions_submitted", False)
        self.set_state("selected_product", None)
        self.set_state("checked_reviews", False)
        self.set_state("show_restart_button", False)

    def add_message(self, role, content, callback=None):
        self.get_state("messages").append({"role": role, "content": content, "callback": callback})

    def set_state(self, key, value):
        st.session_state[key] = value
    
    def get_state(self, key):
        return st.session_state[key]
