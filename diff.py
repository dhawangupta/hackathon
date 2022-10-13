import yaml
import json
from urllib.request import urlopen
from flatten_json import flatten


def oasspec3():  # "operationId": "root__get", "responses": {"200": {"description": "Successful Response", "content": {"application/json": {"schema": {}}}}}}}}}

    newUrl = "https://raw.githubusercontent.com/dhawangupta/hackathon/main/newAPI.json"
    oldUrl = "https://raw.githubusercontent.com/dhawangupta/hackathon/main/oldAPI.json"

    oldResponse = urlopen(newUrl)
    newResponse = urlopen(oldUrl)
    # newresponse = urlopen(url)

    oldApiSpec = json.loads(oldResponse.read())
    newApiSpec = json.loads(newResponse.read())
    # with open('./OASpec/oldAPI.yml', 'r') as file:
    #     configuration =  yaml.safe_load(file)
    # oldApiSpec = json.dumps(configuration)

    # with open('./OASpec/newAPI.yml', 'r') as file:
    #     configuration =  yaml.safe_load(file)
    # newApiSpec = json.dumps(configuration)
    # oldApiSpec = json.loads(oldApiSpec)
    # newApiSpec = json.loads(newApiSpec)
    # print(newApiSpec)
    new_json_list_flattened = flatten(newApiSpec["paths"], '.')
    old_json_list_flattened = flatten(oldApiSpec["paths"], '.')
    l1 = (set(new_json_list_flattened.keys()))
    l2 = (set(old_json_list_flattened.keys()))
    count = 0
    if (len(l1 ^ l2) != 0):
        return False
    else:
        for i in new_json_list_flattened:
            if i.endswith(".type"):
                if (new_json_list_flattened[i] != old_json_list_flattened[i]):
                    count = count + 1
            if i.endswith(".required"):
                if (str(new_json_list_flattened[i]) != old_json_list_flattened[i]):
                    count = count + 1

        return False if (count > 0) else True


print(oasspec3())