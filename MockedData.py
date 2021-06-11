import json

def getTestData(filename):
    TEST_DATA = []

    with open(filename,'r') as f:
        TEST_DATA=json.load(f) # json.dump json.loads json.dumps
    return TEST_DATA