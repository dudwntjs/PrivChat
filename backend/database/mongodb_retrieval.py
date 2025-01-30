import json
import requests
from pymongo import MongoClient
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from dotenv import load_dotenv
import os

# 환경 변수 로드
load_dotenv()
clova_api_key = os.getenv("CLOVA_API_KEY")

# ✅ MongoDB 연결
client = MongoClient("mongodb://localhost:27017/")
db = client["law_database"]
cases_collection = db["cases"]

# ✅ HyperCLOVA X 임베딩 API 호출 함수
def generate_embedding(text):
    url = "https://clovastudio.stream.ntruss.com/testapp/v1/api-tools/embedding/clir-emb-dolphin/{app-id}"  
    headers = {
        "Authorization": f"Bearer {clova_api_key}",  # ✅ Bearer 인증 방식 적용
        "Content-Type": "application/json; charset=utf-8"
    }
    payload = {
        "text": text
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()["result"]["embedding"]  # ✅ 1024차원 벡터 반환
    else:
        print(f"❌ 오류 발생: {response.json()}")
        return None

# ✅ 판례 데이터를 벡터화하여 FAISS에 저장하는 함수
def vectorize_cases():
    documents = []
    cases = cases_collection.find({}, {"_id": 0, "판례일련번호": 1, "판결요지": 1}).limit(100)

    for case in cases:
        case_text = f"판례일련번호: {case['판례일련번호']}\n{case['판결요지']}"
        embedding_vector = generate_embedding(case_text)  # ✅ HyperCLOVA X 임베딩 호출

        if embedding_vector:
            doc = Document(page_content=case_text, metadata={"id": case["판례일련번호"], "embedding": embedding_vector})
            documents.append(doc)

    # ✅ FAISS 벡터 저장소 생성 및 저장
    vectorstore = FAISS.from_documents(documents, embedding=embedding_vector)  
    vectorstore.save_local("faiss_index")

    print("✅ 벡터 저장소 생성 완료!")

# ✅ 데이터 벡터화 실행
if __name__ == "__main__":
    vectorize_cases()