import requests
import sys
sys.path.append("")
import utils

NETLIFY_TOKEN = utils.getConfig('netlifyToken')
NETLIFY_USER = utils.getConfig('netlifyUser')
BASE_NETLIFY_ENDOPOINT = "https://api.netlify.com"

def getDeployKey():
    response = netlifyRequest("/api/v1/deploy_keys")
    
    if(response.ok):
        return response.json()['public_key']
    else:
        return response.raise_for_status()
    

def netlifyRequest(url, contentType="application/json",json={},method="POST"):
    reqUrl = BASE_NETLIFY_ENDOPOINT + url
    response = requests.request(
        method,
        url=reqUrl,
        headers={
            "content-type": contentType,
            "Authorization": "Bearer "+NETLIFY_TOKEN
        },
        json=json
    )
    return response