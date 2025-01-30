from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ai.hyperclova import HyperCLOVAExecutor  # ✅ 커스텀 클래스 임포트

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

# ✅ HyperCLOVA X 실행기 인스턴스 생성
clova_executor = HyperCLOVAExecutor()

# 요청 데이터 모델
class QueryRequest(BaseModel):
    query: str

# 판례 검색 API
@app.post("/search/")
async def search_case(request: QueryRequest):
    clova_answer = clova_executor.generate_answer(request.query)
    return {"clova_answer": clova_answer}

# 서버 실행 코드
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)