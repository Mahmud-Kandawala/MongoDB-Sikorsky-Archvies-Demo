# setup_database.py

from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('localhost', 27017)

# Create a new database
db = client['sikorsky_archives']

# Create a new collection
collection = db['sample_data']

# Insert sample data
sample_data = [
    {"name": "Document 1", "type": "Report", "size": "2GB"},
    {"name": "Document 2", "type": "Manual", "size": "3GB"}
]

collection.insert_many(sample_data)

print("Database setup completed successfully.")
