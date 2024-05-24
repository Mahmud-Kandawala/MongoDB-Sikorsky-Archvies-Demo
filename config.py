import os 
from pymongo import MongoClient


# MONGODB SETTINGS #

######################

# Establish base path so it applies where it is mentioned over all files.

base_path = r'E:\DOWNLOAD FILES' 

# Store variables for mongodb connection that persists over all files.

client = MongoClient('localhost', 27017)
db = client['sikorsky_archives']

'''Returns a list of all folder names (and not anything inside of them)
inside of the base directory. These line up with collection names as the system currently stands.'''

collection_names = os.listdir(base_path) 


# TRANSCRIPTION MODULE SETTINGS (PDF OCR) #

######################

######################