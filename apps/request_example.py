import requests
# r = requests.post('http://127.0.0.1:8082/extract_table_serv', files={"file": open('example-page.png', 'rb')})
from loguru import logger

url = "http://127.0.0.1:8082/extract_table_serv"
# r = requests.get('http://127.0.0.1:8080/')
file_path = 'example-page.png'
with open(file_path, 'rb') as f:
    files = {'file': f}
    logger.debug("file taken")
    response = requests.post(url, files=files)
# print(r.text)
print(response.text)