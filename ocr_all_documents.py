import os
from pymongo import MongoClient
import logging
from config import *

# Empty for now, will work on it come Sunday, or perhaps Saturday after work.

# How this will be intended to work is to find the file path of any .pdfs, OCR them, and save the OCR'd document as the PDF, overwriting it. Will of course be done on 
# a version of the data where I can afford to make mistakes [no screwing up the master copies].