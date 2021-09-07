import requests
import os
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv('ACCESS_TOKEN')

# print(access_token)

my_headers = {'Authorization' : 'Bearer {}'.format(access_token)}
data = {'event_type': 'deploy'}

# print(my_headers)

r = requests.post('https://api.github.com/repos/AAInternal/herc-kronos/dispatches', json=data, headers=my_headers)
print(r)