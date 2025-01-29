from pymongo import MongoClient

# MongoDB 연결
MONGO_URL = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URL)

# 사용할 데이터베이스 & 컬렉션
db = client["law_database"]
cases_collection = db["cases"]
decisions_collection = db["decisions"]
personal_info_collection = db["personal_info"]