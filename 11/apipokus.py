import requests
import json

with open('token.txt') as soubor:
    token = soubor.read().strip()

headers = {'Authorization': 'token ' + token}

stranka = requests.put('https://api.github.com/user/starred/pyvec/naucse.python.cz', headers=headers)

print(stranka.status_code)

