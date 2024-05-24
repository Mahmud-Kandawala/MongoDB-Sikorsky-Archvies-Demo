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

        try: # Tries to make the new proposed file path. If it fails, then the file name is null, and would throw an error.
            new_path = os.path.join(base_path, collection_name.replace(' ', '_'), filename) 
        except: # If an error from the above statement, break and restart the loop with the next filename.
            logging.warning(f"No fileLink found for document ID {document['_id']} in collection {collection_name}") # Break and restart the loop with the next filename.
            break

        if ('.' not in os.path.split(new_path)[-1]): # Splits the proposed new path by the slashes, if the last one does not have a '.' (which also means no file extension), break.
            logging.warning(f"No fileLink found for document ID {document['_id']} in collection {collection_name}")
            break

        try: # After passing all the above checks, program is allowed to replace the file path with the proposed file path. 
            collection.update_one({'_id': document['_id']}, {'$set': {'fileLink': new_path}})
            logging.info(f"Updated fileLink for document ID {document['_id']} in collection {collection_name} to {new_path}")

        except Exception as e: # To catch any other errors, for now. 
            logging.error(f"Failed to update document ID {document['_id']} in collection {collection_name}: {e}")

# Close the connection to MongoDB
client.close() 
