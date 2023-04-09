import time
import random
import datetime
import requests

for i in range(1):
    #post
    volt = random.randrange(8, 12)
    time_instance = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    data = {"volt": volt, "time_instance": time_instance, "bill_no": "SS001"}


    url = 'http://127.0.0.1:8000/api/v1/'
    x = requests.get(url, json={'id':1})
    data = x.json()
    print(data)
    # time.sleep(2)