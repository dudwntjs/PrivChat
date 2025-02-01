from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv, find_dotenv

# FastAPI 애플리케이션 생성
app = FastAPI()

# ✅ CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 환경 변수 로드
dotenv_path = find_dotenv()  # .env 파일을 자동으로 찾습니다.
if not dotenv_path:
    raise FileNotFoundError("❌ .env 파일을 찾을 수 없습니다.")
load_dotenv(dotenv_path)  # .env 파일 로드

# OpenAI API Key 로드
openai_api_key = os.getenv("OPENAI_API_KEY")

# OpenAI 임베딩 사용
embedding_model = OpenAIEmbeddings(model="text-embedding-ada-002")

# FAISS 벡터 저장소 로드 함수
def load_vector_store():
    faiss_index_path = os.path.join(os.getcwd(), "database", "faiss_index")
    vectorstore = FAISS.load_local(faiss_index_path, embedding_model, allow_dangerous_deserialization=True)
    return vectorstore

# 쿼리 검색 함수
def search_query(query, vectorstore, k=5):
    search_results = vectorstore.similarity_search(query, k)
    return search_results

class QueryRequest(BaseModel):
    query: str

# 생성형 AI 응답 생성 및 관련 판례 검색
@app.post("/search/")
async def search_case(request: QueryRequest):
    # FAISS 벡터 저장소 로드
    vectorstore = load_vector_store()
    
    # 검색된 판례들
    results = search_query(request.query, vectorstore, k=5)

    # 검색된 판례를 이용한 AI 답변 생성
    search_content = " ".join([result.page_content[:300] for result in results])

    # 생성형 AI 답변을 위한 프롬프트 설정
    prompt_template = """다음은 관련 판례들입니다. 이 판례들을 바탕으로 질문에 답변해주세요:

    {search_content}

    질문: {query}

    답변: """

    prompt = PromptTemplate(input_variables=["search_content", "query"], template=prompt_template)
    
    # 생성형 모델 실행
    llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key)

    # RetrievalQA 체인 생성
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever(), chain_type="stuff")

    # AI 답변 생성
    ai_response = chain({"query": request.query})

    # 관련 판례 목록 생성
    related_cases = [result.page_content[:300] for result in results]

    return {
        "response": ai_response["result"],  # AI의 생성된 답변
        "related_cases": related_cases
    }