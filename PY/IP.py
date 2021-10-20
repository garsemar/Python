import json
import requests
from requests.structures import CaseInsensitiveDict


# https://stackoverflow.com/questions/40827356/find-a-value-in-json-using-python
# https://myprojects.geoapify.com/api/HlB7k9Z7VEAv61XxeoWz/keys
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    for i in text:
        print(i['state'])
    print(text)


url = "https://api.geoapify.com/v1/ipinfo?&apiKey=4e9a19bda1f94bed9b57f7ff04b82a6c"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

resp = requests.get(url, headers=headers)

jprint(resp.json())
