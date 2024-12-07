import streamlit as st
from datetime import datetime

def scroll_to_bottom():
    scroll_script = """
    <script>
        var body = window.parent.document.getElementById("root");
        body.scrollTop += 9999999999;
    </script>
    """
    st.components.v1.html(scroll_script)


# 현재 시간 기반 고유 ID 생성
def generate_short_id():
    return datetime.now().strftime('%Y%m%d%H%M%S%f')