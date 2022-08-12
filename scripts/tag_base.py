import json
import requests

def tag_call(url, req_type="GET", data=""):

    payload={}
    headers = {
    'Authorization': 'creds_go_here',
    'Content-Type': 'application/json'
    }

    response = requests.request(req_type, url, headers=headers, data=data)

    return(json.loads(response.text))

