import requests


with open("/home/roberta/loko/projects/table_extractor/data/foo.pdf", "rb") as f:
    files = {'files': f}

    response = requests.post("http://127.0.0.1:8082/extract_table2", files=files).json()

    data = response
    print(data)
