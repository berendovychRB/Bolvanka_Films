from pymongo import MongoClient

client = MongoClient("mongodb://test:test@mongodb:27017")
db = client.films
