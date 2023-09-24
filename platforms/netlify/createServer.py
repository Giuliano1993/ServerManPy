import requests
import datetime
import time
import json
import netlifyUtils
#from ../../ import utilities.utils
import sys
sys.path.append("")		# fixes import issues

import utils


token = netlifyUtils.NETLIFY_TOKEN
user = netlifyUtils.NETLIFY_USER
sitename = str(time.time())+"site"
payload = {"name":sitename,"subdomain":sitename}
response = netlifyUtils.netlifyRequest(f'/api/v1/{user}/sites', json=payload)

if(response.ok):
    print("New server was correctly created")
    print("New server ID = " + response.json()['id'])
else:
    print("There was an error:")
    print(response.status_code + " : " + response.reason)