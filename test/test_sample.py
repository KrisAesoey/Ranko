# test file for running pytest library
# to test run pip install pytest and any file
# # with test_ or _test.py will be included in run
def func(x):
    return x + 1

def test_answer():
    assert func(4) == 5