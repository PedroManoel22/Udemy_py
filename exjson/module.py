import os
import json

# pessoas = [
#     {"name": "Pedro", "lastname": "Manoel"},
#     {"name": "José", "lastname": "Luiz"},
#     {"name": "Hahah", "lastname": "Miranda"}
# ]

# BASE_DIR = os.path.dirname(__file__)
# SAVE_TO = os.path.join(BASE_DIR, 'arquivo-pyhton.json')

# with open(SAVE_TO, 'w') as file:
#     json.dump(pessoas, file, indent=2)

# print(json.dumps(pessoas, indent=2))

# puxando os dados do arquivo para ca 

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, 'arquivo-pyhton.json')

with open(JSON_FILE, 'r') as file:
    pessoas = json.load(file)
    print(json.dumps(pessoas))
    
    # for pessoa in pessoas:
    #     print(pessoa['name'])