from pymongo import MongoClient
import os

# If you used export, you can access it like this:
mongo_url = os.getenv("MONGODB_URL")

try:
    client = MongoClient(mongo_url)
    # Test the connection by listing databases
    print("Connected! Databases:")
    print(client.list_database_names())
except Exception as e:
    print("Connection failed:", e)
