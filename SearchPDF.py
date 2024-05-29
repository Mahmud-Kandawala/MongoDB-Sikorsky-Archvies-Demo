from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')
db = client['sikorsky_archives']
collection = db['T01.10 Handouts']

# Search for documents containing a specific keyword in the extracted text
keyword = "New York City"
results = collection.find({"extractedText": {"$regex": keyword, "$options": "i"}})

print(f"Documents containing the keyword '{keyword}':")
for doc in results:
    print(f"ID: {doc['_id']}, Title: {doc.get('title', 'No Title')}")

# Close the connection to MongoDB
client.close()



#Search in MongoDB:
#{ "_id": ObjectId("") }