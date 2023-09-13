import requests
import datetime
#from ../../ import utilities.utils
import sys
sys.path.append("")		# fixes import issues

import utils


token = utils.getConfig('netlifyToken')
user = utils.getConfig('netlifyUser')
response = requests.post(
    url=f'https://api.netlify.com/api/v1/{user}/sites',
    headers={
        "content-type": "application/json",
        "Authorization": "Bearer "+token
    },
    data= {
        'name':str(datetime.datetime.now().timestamp())+"site",   
        'subdomain':str(datetime.datetime.now().timestamp())+"site",   
    }
)

print(response.text)