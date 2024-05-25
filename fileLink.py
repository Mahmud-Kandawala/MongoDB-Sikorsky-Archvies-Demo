import os
from pymongo import MongoClient
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')
db = client['sikorsky_archives']

# Define the list of collection names
collection_names = [
    'T01.05 CDs', 'T01.98 Miscellaneous', 'T01.01 16mm_Films', 'T01.02 8mm_Films',
    'T01.03 Aircraft_Material', 'T01.04 Booklets', 'T01.05 CDs', 'T01.06 DVDs',
    'T01.07 Equipment', 'T01.08 Files', 'T01.09 Flat_Documents', 'T01.10 Handouts',
    'T01.11 IIS_Personal_Files', 'T01.12 LP_Records', 'T01.13 Manuals', 'T01.14 Models',
    'T01.15 Negatives', 'T01.16 Notebooks', 'T01.17 Paintngs', 'T01.19 Periodicals',
    'T01.29 Sikorsky_Articles', 'T01.30 Calendars', 'T01.31 Scrapbooks', 'T01.32 Wall_Hangings',
    'T01.33 Rescue_Awards', 'T01.35 Chance_Vought', 'T01.36 Posters', 'T01.37 Pins',
    'T01.38 People_Of_Interest', 'T01.39 Papers', 'T01.40 Picture_Boards', 'T01.41 Beta_Cam_Tapes',
    'T01.42 3-quarter Inch_Tapes', 'T01.43 1-inch_Tapes', 'T01.44 35mm Film and Microfilm',
    'T01.45 Microfiche', 'T01.46 Safe', 'T01.47 Audio_Tapes', 'T01.98 Miscellaneous'
]

# Define the base path where your files are stored
base_path = r'E:\\Hank Sample File - Copy\DATABASE PROJECT\DOWNLOAD FILES\\'

# Iterate through each collection
for collection_name in collection_names:
    logging.info(f"Processing collection: {collection_name}")
    collection = db[collection_name]

    # Update fileLink for each document in the collection
    for document in collection.find():
        filename = document.get('fileLink')
        if filename:
            # Construct the new path with collection name included
            new_path = os.path.join(base_path, collection_name.replace(' ', '_'), filename)
            try:
                collection.update_one({'_id': document['_id']}, {'$set': {'fileLink': new_path}})
                logging.info(f"Updated fileLink for document ID {document['_id']} in collection {collection_name} to {new_path}")
            except Exception as e:
                logging.error(f"Failed to update document ID {document['_id']} in collection {collection_name}: {e}")
        else:
            logging.warning(f"No fileLink found for document ID {document['_id']} in collection {collection_name}")

# Close the connection to MongoDB
client.close()
