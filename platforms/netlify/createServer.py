import requests
import datetime
import time
import json
#from ../../ import utilities.utils
import sys
sys.path.append("")		# fixes import issues

import utils


token = utils.getConfig('netlifyToken')
user = utils.getConfig('netlifyUser')
sitename = str(time.time())+"site"
payload = {"name":sitename,"subdomain":sitename}
response = requests.post(
    url=f'https://api.netlify.com/api/v1/{user}/sites',
    headers={
        "content-type": "application/json",
        "Authorization": "Bearer "+token
    },
    json=payload
)

if(response.ok):
    print("New server was correctly created")
else:
    print("There was an error:")
    print(response.status_code + " : " + response.reason)