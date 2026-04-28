import json

DATA_PATH = "data.json"

def read_data():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def write_data(data):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)