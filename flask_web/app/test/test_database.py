import time
from pymongo import MongoClient
import random

topic = 'humidity'


host = 'localhost'
port = 27017
mongo_client = MongoClient(host=host, port=port)
db = mongo_client['data']
collection = db['test_humidity']

while True:
    data_save = {
        'topic': topic,
        'data': random.randint(0, 50),
        'timestamp': time.time()
    }
    print(data_save)
    collection.insert(data_save)
    time.sleep(5)
