from pathlib import Path
import sys
# this needs to be optimized or standardized
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)
from src import matchup

def test_item_creation():
    test_dic = { "name" : "test", "extra" : "something", "bonus" : "other" }
    test_item = matchup.Item(test_dic)
    assert test_item.name == "test"
    assert test_item.info == { "extra" : "something", "bonus" : "other" }
    assert test_item.elo == 0.5