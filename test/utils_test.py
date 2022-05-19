from pathlib import Path
import sys
# this needs to be optimized or standardized
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)
from utils import utils

def test_JSON_file_to_dic():
    json_file = "pokemon"
    test_dir = utils.JSON_file_to_dic(json_file)
    assert test_dir[0]["name"] == "Bulbasaur"

def test_JSON_string_to_dic():
    test_string = """
    {
        "test_id": "test_item"
    }
    """
    test_dir = utils.JSON_string_to_dic(test_string)
    assert test_dir["test_id"] == "test_item"