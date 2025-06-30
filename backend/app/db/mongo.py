from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)

# For future use
db = client["app_db"]
