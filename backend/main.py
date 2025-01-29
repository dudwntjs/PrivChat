from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# ✅ CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인에서 요청 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용 (GET, POST, DELETE 등)
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)

# 요청 데이터 모델
class QueryRequest(BaseModel):
    query: str

# 판례 검색 API
@app.post("/search/")
async def search_case(request: QueryRequest):
    return {"message": f"'{request.query}'에 대한 판례 검색 결과입니다."}

# 서버 실행을 위한 코드 (uvicorn으로 실행 가능)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)