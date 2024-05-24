import os
from pymongo import MongoClient
import logging
from config import *



# Refer to config.py to see where client connection went.


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Iterate through each collection
for collection_name in collection_names: # Refer to config.py
    logging.info(f"Processing collection: {collection_name}")
    collection = db[collection_name]
    # Update fileLink for each document in the collection
    for document in collection.find():
        filename = document.get('fileLink')

        try: 
            if type(filename) is not 'NoneType': # AKA don't let it through if 'if fileLink doesn't exist'
                pass
            else:
                root, ext = os.path.splitext(filename) # Check if os can split the filename into both its root and file extension. Throws an error if not.
        except:
            pass

        if filename and ('No link provided' not in filename):
            # Construct the new path with collection name included
            try:
                new_path = os.path.join(base_path, collection_name.replace(' ', '_'), filename)
                collection.update_one({'_id': document['_id']}, {'$set': {'fileLink': new_path}})
                logging.info(f"Updated fileLink for document ID {document['_id']} in collection {collection_name} to {new_path}")
            except Exception as e:
                logging.error(f"Failed to update document ID {document['_id']} in collection {collection_name}: {e}")
        else:
            logging.warning(f"No fileLink found for document ID {document['_id']} in collection {collection_name}")
            collection.update_one({'_id': document['_id']}, {'$set': {'fileLink': 'No link provided'}})

# Close the connection to MongoDB
client.close()
