import requests
import json

base_url = "https://issues.apache.org/jira/rest/api/2"
path = "/issue/ZOOKEEPER-2613"



r = requests.get(base_url + path, verify=False)
r.json()
json_dict = r.json() # a standard python dictionary
print(json.dumps(json_dict, indent=3)) # to pretty-print with 3 spaces of indentation

print(json_dict["fields"]["description"])
