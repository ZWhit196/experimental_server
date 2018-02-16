import json

def _Request_data(rd):
    rd = rd.decode("utf-8")
    return json.loads(rd)