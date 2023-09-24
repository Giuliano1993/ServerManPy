import requests
from netlifyUtils import BASE_NETLIFY_ENDOPOINT, NETLIFY_TOKEN, NETLIFY_USER,getDeployKey
import sys
sys.path.append("")
import utils

# following this process in order to create the deploy
#https://answers.netlify.com/t/deploy-the-github-repo-using-api/24269/2

pk = getDeployKey()

site_id = ""
url = BASE_NETLIFY_ENDOPOINT + f"/api/v1/sites/{site_id}/deploys"