from pymongo import MongoClient

client = MongoClient()
db = client.films
films_collection = db["films"]
