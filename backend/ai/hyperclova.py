import os
import json
import requests
from dotenv import load_dotenv

# ✅ 환경 변수 로드
load_dotenv()
clova_api_key = os.getenv("CLOVA_API_KEY")  # .env에서 API 키 불러오기

class HyperCLOVAExecutor:
    def __init__(self):
        """HyperCLOVA API 요청을 처리하는 클래스"""
        self.api_key = clova_api_key  # ✅ .env에서 불러온 API 키 사용
        self.api_url = "https://clovastudio.stream.ntruss.com/testapp/v1/chat-completions/HCX-003"

    def generate_answer(self, query: str):
        """사용자의 질문을 HyperCLOVA X에 요청하여 답변을 생성"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",  # ✅ 최신 인증 방식 적용
            "Content-Type": "application/json; charset=utf-8"
        }

        payload = {
            "messages": [
                {"role": "system", "content": "참고 자료를 바탕으로 답변을 생성하세요."},
                {"role": "user", "content": query}
            ],
            "topP": 0.6,
            "topK": 0,
            "maxTokens": 1024,
            "temperature": 0.5,
        }

        response = requests.post(self.api_url, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json().get("result", {}).get("text", "답변 생성 실패")
        else:
            print(f"❌ 오류 발생: {response.json()}")
            return "오류 발생"

# ✅ 테스트 코드
if __name__ == "__main__":
    executor = HyperCLOVAExecutor()
    response = executor.generate_answer("대한민국의 헌법은?")
    print(response)  # ✅ HyperCLOVA X의 답변 출력