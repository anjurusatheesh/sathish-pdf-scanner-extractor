# backend/app/services/mongodb_service.py
from pymongo import MongoClient
# from config import settings
from app.config import settings

client = MongoClient(settings.MONGODB_URL)
db = client[settings.DATABASE_NAME]
collection = db["extracted_data"]

def insert_document(document: dict):
    return collection.insert_one(document)