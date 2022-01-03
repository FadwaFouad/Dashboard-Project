import logging
import time
import random
import threading

import requests

endpoints = ('', 'api','test','error','error2','error3')

def run():
    while True:
        try:
            target = random.choice(endpoints)
            requests.get("http://backend:8081/%s" % target, timeout=1)
            logging.info(endpoints)
            target = random.choice(endpoints)
            requests.get("http://frontend:8080/%s" % target, timeout=1)
            logging.info(endpoints)
        except:
            pass


if __name__ == '__main__':
    logging.basicConfig(format="%(message)s", level=logging.INFO)
    for _ in range(4):
        thread = threading.Thread(target=run)
        thread.daemon = True
        thread.start()

    while True:
        time.sleep(1)

