import os
import json
from database.db import cases_collection, decisions_collection, personal_info_collection

# 📌 데이터 경로
BASE_DIR = "/Users/sunyoungju/legal_text_analysis_data"

# 📌 판례 데이터 저장 함수
def insert_cases_data():
    cases_path = os.path.join(BASE_DIR, "01_raw_data", "1_cases")
    if not os.path.exists(cases_path):
        raise FileNotFoundError(f"❌ 경로를 찾을 수 없습니다: {cases_path}")

    for file in os.listdir(cases_path):
        if file.endswith(".json"):
            with open(os.path.join(cases_path, file), "r", encoding="utf-8") as f:
                data = json.load(f)
                
                # ✅ 고유 ID 키 확인
                if "판례일련번호" not in data:
                    print(f"⚠️ {file} 에서 '판례일련번호' 필드를 찾을 수 없습니다. 스킵합니다.")
                    continue
                
                data["출처"] = "legal_text_analysis_data/01_raw_data/1_cases"
                cases_collection.update_one({"판례일련번호": data["판례일련번호"]}, {"$set": data}, upsert=True)
                print(f"✅ 판례 저장 완료: {file}")

# 📌 행정심판 데이터 저장 함수
def insert_decisions_data():
    decisions_path = os.path.join(BASE_DIR, "01_raw_data", "2_decisions")
    if not os.path.exists(decisions_path):
        raise FileNotFoundError(f"❌ 경로를 찾을 수 없습니다: {decisions_path}")

    for file in os.listdir(decisions_path):
        if file.endswith(".json"):
            with open(os.path.join(decisions_path, file), "r", encoding="utf-8") as f:
                data = json.load(f)
                
                # ✅ 고유 ID 키 확인
                if "행정심판재결례일련번호" not in data:
                    print(f"⚠️ {file} 에서 '행정심판재결례일련번호' 필드를 찾을 수 없습니다. 스킵합니다.")
                    continue
                
                data["출처"] = "legal_text_analysis_data/01_raw_data/2_decisions"
                decisions_collection.update_one({"행정심판재결례일련번호": data["행정심판재결례일련번호"]}, {"$set": data}, upsert=True)
                print(f"✅ 행정심판 데이터 저장 완료: {file}")

# 📌 개인정보 라벨링 데이터 저장 함수
def insert_personal_info_data():
    personal_info_path = os.path.join(BASE_DIR, "02_labeled_data", "personal_info")
    if not os.path.exists(personal_info_path):
        raise FileNotFoundError(f"❌ 경로를 찾을 수 없습니다: {personal_info_path}")

    for file in os.listdir(personal_info_path):
        if file.endswith(".json"):
            with open(os.path.join(personal_info_path, file), "r", encoding="utf-8") as f:
                data = json.load(f)
                
                # ✅ 고유 ID 키 확인
                if "info" not in data or "id" not in data["info"]:
                    print(f"⚠️ {file} 에서 'id' 필드를 찾을 수 없습니다. 스킵합니다.")
                    continue
                
                data["출처"] = "legal_text_analysis_data/02_labeled_data/personal_info"
                personal_info_collection.update_one({"id": data["info"]["id"]}, {"$set": data}, upsert=True)
                print(f"✅ 개인정보 라벨링 데이터 저장 완료: {file}")

# 📌 실행 함수
def run():
    insert_cases_data()
    insert_decisions_data()
    insert_personal_info_data()
    print("📌 모든 Training 데이터 MongoDB 저장 완료!")

# 📌 실행
if __name__ == "__main__":
    run()