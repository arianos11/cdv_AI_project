import json
import os

def readFile(path):
    file = open(path)
    data = json.load(file)
    return data

def readLevels():
    return os.listdir('./levels')
