import yaml
import json
from urllib.request import urlopen
from flatten_json import flatten

# oldApiSpec = {"openapi": "3.0.2", "info": {"title": "FastAPI", "version": "0.1.0"}, "paths": {"/": {"get": {"summary": "Root",
def oasspec3():                                                                                                           # "operationId": "root__get", "responses": {"200": {"description": "Successful Response", "content": {"application/json": {"schema": {}}}}}}}}}
    # oldApiSpec = {"openapi": "3.0.2", "info": {"title": "Custom title", "description": "This is a very custom OpenAPI schema", "version": "2.5.0", "x-logo": {"url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"}}, "paths": {"/root{category}/{name}": {"get": {"summary": "Root", "operationId": "root_root_category___name__get", "parameters": [{"required": "true", "schema": {"title": "Category", "type": "string"}, "name": "category", "in": "path"}, {"required": "true", "schema": {"title": "Name", "type": "string"}, "name": "name", "in": "path"}], "responses": {"200": {"description": "Successful Response", "content": {"application/json": {"schema": {}}}}, "422": {"description": "Validation Error", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/HTTPValidationError"}}}}}}}, "/branch{category}/{name}": {"get": {"summary": "Branch", "operationId": "branch_branch_category___name__get", "parameters": [{"required": "true", "schema": {
    #     "title": "Category", "type": "string"}, "name": "category", "in": "path"}, {"required": "true", "schema": {"title": "Name", "type": "string"}, "name": "name", "in": "path"}], "responses": {"200": {"description": "Successful Response", "content": {"application/json": {"schema": {}}}}, "422": {"description": "Validation Error", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/HTTPValidationError"}}}}}}}}, "components": {"schemas": {"HTTPValidationError": {"title": "HTTPValidationError", "type": "object", "properties": {"detail": {"title": "Detail", "type": "array", "items": {"$ref": "#/components/schemas/ValidationError"}}}}, "ValidationError": {"title": "ValidationError", "required": ["loc", "msg", "type"], "type": "object", "properties": {"loc": {"title": "Location", "type": "array", "items": {"type": "string"}}, "msg": {"title": "Message", "type": "string"}, "type": {"title": "Error Type", "type": "string"}}}}}}
    # oldApiSpec = {"openapi":"3.0.2","info":{"title":"FastAPI","version":"0.1.0"},"paths":{"/root{category}/{name}":{"get":{"summary":"Root","operationId":"root_root_category___name__get","parameters":[{"required":"true","schema":{"title":"Category","type":"string"},"name":"category","in":"path"},{"required":"true","schema":{"title":"Name","type":"string"},"name":"name","in":"path"}],"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}}},"/branch{category}":{"get":{"summary":"Branch","operationId":"branch_branch_category__get","parameters":[{"required":"true","schema":{"title":"Category","type":"string"},"name":"category","in":"path"},{"required":"true","schema":{"title":"Name","type":"string"},"name":"name","in":"query"}],"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}}}},"components":{"schemas":{"HTTPValidationError":{"title":"HTTPValidationError","type":"object","properties":{"detail":{"title":"Detail","type":"array","items":{"$ref":"#/components/schemas/ValidationError"}}}},"ValidationError":{"title":"ValidationError","required":["loc","msg","type"],"type":"object","properties":{"loc":{"title":"Location","type":"array","items":{"type":"string"}},"msg":{"title":"Message","type":"string"},"type":{"title":"Error Type","type":"string"}}}}}}
    # url = "http://127.0.0.1:8000/openapi.json"

    # newresponse = urlopen(url)

    # newApiSpec = json.loads(newresponse.read())
    with open('./OASpec/oldAPI.yml', 'r') as file:
        configuration =  yaml.safe_load(file)
    oldApiSpec = json.dumps(configuration)

    with open('./OASpec/newAPI.yml', 'r') as file:
        configuration =  yaml.safe_load(file)
    newApiSpec = json.dumps(configuration)
    oldApiSpec = json.loads(oldApiSpec)
    newApiSpec = json.loads(newApiSpec)
    print(newApiSpec)
    new_json_list_flattened = flatten(newApiSpec["paths"], '.')
    old_json_list_flattened = flatten(oldApiSpec["paths"], '.')
    l1 = (set(new_json_list_flattened.keys()))
    l2 = (set(old_json_list_flattened.keys()))
    # print(len(l1))
    # print(len(l2))
    count = 0
        # print(list(new_json_list_flattened.keys()) - list(old_json_list_flattened.keys()))
    # print("jhdbrjb", len(l2 ^ l1))
    if(len(l1 ^ l2) != 0):
        return False
    else:
            for i in new_json_list_flattened:
                if i.endswith(".type"):
                    if(new_json_list_flattened[i] != old_json_list_flattened[i]):
                        count = count + 1
                if i.endswith(".required"):
                    # if(type(new_json_list_flattened[i]) == bool):
                    #     if new_json_list_flattened[i] == True:
                    #         new_json_list_flattened[i] = "true"
                    #     else:
                    #         new_json_list_flattened[i] = "false"
                    print(new_json_list_flattened[i])
                    print(old_json_list_flattened[i])
                    if(str(new_json_list_flattened[i]) != old_json_list_flattened[i]):
                        count = count + 1   
                             
            return False if(count > 0) else True
# if len(jsondiff.diff(new_path_key, old_path_key)) != 0:
#     difference.append((jsondiff.diff(new_path_key, old_path_key)))
#     print("diff = ",(jsondiff.diff(new_path_key, old_path_key)))
# else:
#     for i in new_path_key:
#         # endpoint type
#         if(len(jsondiff.diff(newApiSpec["paths"].get(i).keys(), oldApiSpec["paths"].get(i).keys())) != 0):
#             print(jsondiff.diff(newApiSpec["paths"].get(i).keys(), oldApiSpec["paths"].get(i).keys()))
        


# print(oldApiSpec["paths"])
# elif (jsondiff.diff(oldApiSpec.get(old_path_key).values(), newApiSpec.get("paths").keys(), syntax="explicit")):
print(oasspec3())
