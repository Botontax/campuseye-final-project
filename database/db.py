import json

def read_data():
    with open("data.json", "r", encoding="utf-8") as f:
        return json.load(f)

def write_data(data):
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)