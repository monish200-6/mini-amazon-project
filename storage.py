import json
import os

def load_data(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)