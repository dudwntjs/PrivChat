import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient

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

# OpenAI 임베딩 사용
embedding_model = OpenAIEmbeddings(model="text-embedding-ada-002")

# FAISS 벡터 저장소 로드
def load_vector_store():
    # FAISS 벡터 저장소 불러오기 (allow dangerous deserialization)
    vectorstore = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)
    return vectorstore

# 쿼리 검색 함수
def search_query(query, vectorstore, k=5):
    # 입력된 쿼리를 벡터화하여 검색
    search_results = vectorstore.similarity_search(query, k)
    return search_results

if __name__ == "__main__":
    # FAISS 벡터 저장소 로드
    vectorstore = load_vector_store()

    # 검색 쿼리 예시
    query = "법적 근거에 대해 알려주세요"
    
    # 검색 수행
    results = search_query(query, vectorstore, k=5)

    print(f"🔍 검색 결과 (상위 5개):")
    for result in results:
        print(f"- {result.page_content[:300]}...")  # 결과의 앞 300자 출력