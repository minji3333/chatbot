import streamlit as st

class ChatbotSession:
    def __init__(self):
        self.set_state("messages", [
            {"role": "assistant", "content": "안녕하세요. 사용자 리뷰 기반으로 가전제품을 추천해드리는 챗봇 \"CHATBOT\" 입니다.\n\n어떤 가전제품을 찾고 계신가요? 😊"}
        ])
        self.reset()

    def reset(self):
        default_states = {
            "selected_main_category": None,
            "selected_sub_category": None,
            "custom_sub_category": False,
            "sub_category_input": None,
            "conditions": None,
            "conditions_submitted": False,
            "selected_product": None,
            "checked_reviews": False,
            "show_restart_button": False,
        }

        for key, value in default_states.items():
            self.set_state(key, value)

    def add_message(self, role, content, callback=None):
        self.get_state("messages").append({"role": role, "content": content, "callback": callback})

    def set_state(self, key, value):
        st.session_state[key] = value
    
    def get_state(self, key):
        return st.session_state[key]
