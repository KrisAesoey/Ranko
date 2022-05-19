import json
from pathlib import Path

# methods to load JSON objects

data_path = str(Path('./data')) + '/'

def JSON_string_to_dic(json_string: str):
    """Creates a dictionary from a JSON string"""
    dic = json.loads(json_string)
    return dic

def JSON_file_to_dic(json_file: str):
    """Creates a dictionary from a JSON file"""
    file = open(data_path + json_file + ".json")
    dic = json.load(file)
    return dic

def save_dic_as_JSON(dic: dict, filename: str):
    """Stores dictionary as a JSON file"""
    with open(data_path + filename + ".json", 'w') as file:
        json.dump(dic, file)