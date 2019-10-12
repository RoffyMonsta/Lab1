import requests
import json
import logging
import time
import threading

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def run():
    main("http://localhost:8000/health")

def main(url):
    try:
        r = requests.get(url)
        data = json.loads(r.content)
        logging.info("Current state: %s", data['date'])
        logging.info("Current page: : %s", data['current_page'])
        logging.info("Server's answers:")
        for key in data.keys():
            logging.info("Key: %s, Argument: %s", key, data[key])
        print("IT'S OK")
    except:
        print("No responce")
        logging.error("No responce from server")
        logging.warning("No responce from server")

    
    while True:
        time.sleep(60)
        run();

if __name__ == '__main__':
    run()
