from pymongo import MongoClient

connection_string = "mongodb://192.168.0.10:27017/books"
client = MongoClient(connection_string)
db.client.get_database("books")

collection = db.get_collection("item")

lists = []



response = collection.insert_one(lists)
