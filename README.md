# Chatbot Project 🤖

사용자 리뷰를 기반으로 가전제품을 추천하는 Streamlit 기반의 챗봇 애플리케이션입니다.

---

## 🚀 기능 소개

1. **가전제품 추천**  
   - 사용자 리뷰와 조건을 기반으로 최적의 제품을 추천합니다.
   
2. **조건 입력 및 맞춤형 검색**  
   - 특정 조건을 입력하면 해당 조건에 맞는 제품을 추천합니다.

3. **리뷰 확인**  
   - 추천 제품에 대한 사용자의 리뷰를 확인할 수 있습니다.

4. **최저가 구매 링크 제공**  
   - 제품 구매를 위한 최저가 링크를 제공합니다.

---

## 📂 프로젝트 구조

```plaintext
project/
├── src/
│   ├── __init__.py
│   ├── main.py              # 애플리케이션 엔트리 포인트
│   ├── api/                 # API 관련 코드
│   │   ├── __init__.py
│   │   └── api_client.py    # API 클라이언트 클래스
│   ├── ui/                  # UI 관련 코드
│   │   ├── __init__.py
│   │   ├── renderer.py      # UI 렌더링 클래스
│   │   └── styles.css       # UI 스타일링 파일
│   ├── session/             # 세션 관리 코드
│   │   ├── __init__.py
│   │   └── session.py       # 세션 관리 클래스
│   └── utils/               # 유틸리티 코드
│       ├── __init__.py
│       └── utils.py         # 공용 유틸리티 함수
├── requirements.txt         # 프로젝트 패키지
├── README.md                # 프로젝트 설명 문서
└── .gitignore               # Git에서 무시할 파일
```

---

## 🛠️ 설치 방법

1. **프로젝트 클론**
   ```bash
   git clone https://github.com/your-repo/chatbot-project.git
   cd chatbot-project
   ```

2. **가상 환경 생성 및 활성화**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Mac/Linux
    venv\Scripts\activate     # Windows
    ```

3. **패키지 설치**
    ```bash
    pip install -r requirements.txt
    ```

4. **Streamlit 실행**
    ```bash
    streamlit run src/main.py
    ```

---

## 🖥️ 사용 방법

1. **앱 실행**  
   위의 설치 방법을 따라 Streamlit 서버를 실행합니다.
   
2. **챗봇 사용**  
   - 가전제품의 카테고리를 선택합니다.
   - 원하는 서브 카테고리와 조건을 입력합니다.
   - 추천 제품 및 리뷰를 확인하고 구매 링크를 클릭합니다.

---

## ⚙️ 주요 라이브러리

- **Streamlit**: 웹 애플리케이션 UI 구축.
- **Requests**: API 통신.
- **Pandas**: 데이터 처리.
- **Altair**: 데이터 시각화.

---

## 🗂️ 패키지

다음 패키지는 `requirements.txt`에 명시되어 있습니다.
```
streamlit
streamlit-chat
pandas
tabulate
```

---

## 📌 참고 사항

- **API 설정**: `api_client.py`에서 `BASE_URL`을 사용자의 API 서버 URL로 변경하세요.
- **CSS 파일**: `styles.css` 파일을 수정하여 UI 스타일을 변경할 수 있습니다.
