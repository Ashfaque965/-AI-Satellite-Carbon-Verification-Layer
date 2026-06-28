import json

def format_response(data: dict):
    return json.loads(json.dumps(data))