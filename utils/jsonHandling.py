import json


def jsonHandling(filePath):
    with open(filePath) as data:
        creds = json.load(data)
        return creds