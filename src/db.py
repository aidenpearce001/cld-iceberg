import os
from dotenv import load_dotenv
import pymongo
import pprint

load_dotenv()

MONGODB = os.getenv('MONGODB')

print("MONGO PATH", MONGODB)

client = pymongo.MongoClient(MONGODB)
db = client['chongluadao']


def add_phishing_record(record):
    obj = db["DATA"].find_one({"url": record["url"]})
    if obj is not None:
        return obj
    else:
        return db["DATA"].insert_one(record)
