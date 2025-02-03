# 📜 개인정보 판례 검색 및 요약 시스템 (RAG 기반 AI)  

![스플래시 화면](https://github.com/dudwntjs/PrivChat/blob/main/frontend/assets/Splash.png?raw=true)

**LangChain + LLM 기반 RAG 모델을 활용한 개인정보 판례 검색 & 요약 시스템**  
AI를 통해 개인정보 관련 판례를 검색하고, 법적 판단을 요약하여 제공하는 서비스입니다.

---

## 🚀 주요 기능 (Features)
✔ **RAG 기반 AI 판례 검색** - 유사한 판례를 검색하여 연관된 법적 정보를 제공  
✔ **판례 요약 기능** - LLM을 활용하여 판례 내용을 간결하게 요약  
✔ **MongoDB 데이터 저장** - 판례 데이터 및 검색 결과를 저장하고 관리  
✔ **FAISS 기반 벡터 검색** - OpenAI 임베딩(`text-embedding-ada-002`)을 활용한 고속 검색  
✔ **REST API 지원** - FastAPI 기반의 간편한 API 제공  
✔ **React 프론트엔드** - 직관적인 UI에서 판례 검색 및 결과 확인  

---

## 🛠️ 기술 스택 (Tech Stack)
| 카테고리   | 기술 |
|------------|----------------------------------|
| **Backend** | FastAPI, LangChain, OpenAI API, MongoDB |
| **Frontend** | React, Axios |
| **AI Model** | LangChain + LLM (RAG), OpenAI 임베딩 (`text-embedding-ada-002`), FAISS 벡터 저장소 |

---

## 💻 설치 및 실행 방법 (Installation & Usage)

### 1️⃣ **프로젝트 클론**
```bash
git clone https://github.com/dudwntjs/PrivChat.git
cd PrivChat
```

### 2️⃣ **백엔드 (FastAPI) 실행**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3️⃣ **프론트엔드 (React) 실행**
```bash
cd frontend
npm install
npm start
```

### 4️⃣ **MongoDB 데이터 삽입**
```bash
python backend/mongo_insert.py
```

---

## 🛠️ API 엔드포인트 (Endpoint)
✅ **`POST /search/`** - 입력된 키워드로 판례 검색 및 요약 결과 반환

---

## 📝 질문 예시 (사용자가 할 수 있는 질문)
- "개인정보 유출 시 기업이 받을 법적 처벌은?"
- "개인정보 보호법 위반 시 손해배상 범위는?"
- "비식별화된 데이터도 법적으로 보호받을 수 있는가?"

![채팅 화면](https://github.com/dudwntjs/PrivChat/blob/main/frontend/assets/Chat.png?raw=true)

---
## 🚫 비관련 질문에 대한 응답 제한
- 법률과 무관한 질문에는 답변하지 않음
- 할루시네이션(잘못된 정보 생성) 방지

![채팅 화면2](https://github.com/dudwntjs/PrivChat/blob/main/frontend/assets/Chat2.png?raw=true) 

---

## 📜 라이선스 (License)

📌 **문의:** [sts07190@naver.com](mailto:sts07190@naver.com)

🚀 **이제 프로젝트를 실행하고, AI 기반 판례 검색을 체험해 보세요!** 🔥
