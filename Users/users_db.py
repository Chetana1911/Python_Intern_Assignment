
# Install the pymongo library - pip install pymongo

from pymongo import MongoClient
import datetime

# Create a connection to the MongoDB database
client = MongoClient("mongodb://localhost:27017/")

# Get the database and collection
db = client["dummyapi"]
collection = db["users"]

# Fetch all users data
users = collection.find({})

# Print the users data
for user in users:
    print(user)
