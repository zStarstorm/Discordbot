import requests
import random
id = random.randint(128,70000000)
level = requests.get(f'https://gdbrowser.com/api/level/{id}')
result = level.json()
print(result['level'])