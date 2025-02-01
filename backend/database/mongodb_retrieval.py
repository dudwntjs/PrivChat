import json
import os
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document

# 환경 변수 로드
dotenv_path = find_dotenv()  # .env 파일을 자동으로 찾습니다.
if not dotenv_path:
    raise FileNotFoundError("❌ .env 파일을 찾을 수 없습니다.")

load_dotenv(dotenv_path)  # .env 파일 로드

# OPENAI_API_KEY 환경 변수 로드
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("❌ OPENAI_API_KEY가 .env 파일에 설정되어 있지 않습니다.")

print("✅ OPENAI_API_KEY 로드 완료!")

# MongoDB 연결
client = MongoClient("mongodb://localhost:27017/")
db = client["law_database"]
cases_collection = db["cases"]

# OpenAI 임베딩 사용
embedding_model = OpenAIEmbeddings(model="text-embedding-ada-002")

# 벡터 저장소 생성 함수
def create_vector_store():
    documents = []
    
    # 판례 데이터 불러오기
    cases = cases_collection.find({}, {"_id": 0, "판례일련번호": 1, "판결요지": 1}).limit(100)  # 판결요지만 사용

    for case in cases:
        case_text = f"판례일련번호: {case['판례일련번호']}\n{case['판결요지']}"
        doc = Document(page_content=case_text, metadata={"id": case["판례일련번호"]})
        documents.append(doc)

    # 벡터 저장소 생성
    vectorstore = FAISS.from_documents(documents, embedding_model)
    vectorstore.save_local("faiss_index")

    print("✅ 벡터 저장소 생성 완료!")

# 메인 실행 부분
if __name__ == "__main__":
    create_vector_store()