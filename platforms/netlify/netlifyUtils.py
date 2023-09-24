import requests
import sys
sys.path.append("")
import utils

NETLIFY_TOKEN = utils.getConfig('netlifyToken')
NETLIFY_USER = utils.getConfig('netlifyUser')
BASE_NETLIFY_ENDOPOINT = "https://api.netlify.com"

def getDeployKey():
    response = requests.post(
        url= BASE_NETLIFY_ENDOPOINT+"/api/v1/deploy_keys",
        headers={
            "content-type": "application/json",
            "Authorization": "Bearer "+NETLIFY_TOKEN
        },
        
    )
    if(response.ok):
        return response.json()['public_key']
    else:
        return response.raise_for_status()
    

