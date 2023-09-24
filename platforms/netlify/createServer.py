
import time
import netlifyUtils
import inquirer
#from ../../ import utilities.utils
import sys
sys.path.append("")		# fixes import issues

import utils
from gitScripts import repoList


    

token = netlifyUtils.NETLIFY_TOKEN
user = netlifyUtils.NETLIFY_USER
sitename = str(time.time())+"site"
payload = {
    "name":sitename,
    "subdomain":sitename}


# ask the usere if to link a repo to the site
connectRepo = [inquirer.List('connectRepo', message="Do you want to link a repo to this server?", choices=["Yes","No"])]
linkRepo = inquirer.prompt(connectRepo)['connectRepo']

if(linkRepo == 'Yes'):
    repos = repoList.repoList()
    
    repoChoices = []
    for i, repo in enumerate(repos):
        choice = repo['full_name']
        repoChoices.append(choice)

    chooseRepo = [inquirer.List('pickRepo', message="choose a repo you want to link to the site", choices=repoChoices)]
    answers = inquirer.prompt(chooseRepo)
    index = repoChoices.index(answers['pickRepo'])
    repo = repos[index]
    pk = netlifyUtils.getDeployKey()
    payload['repo'] = {
        "branch": repo['default_branch'],
        "cmd": "npm run build",
        "deploy_key_id": pk,
        "dir": "build/",
        "private": False,
        "provider": "github",
        "repo": repo['full_name'],
        "repo_id": repo['id']
    }
response = netlifyUtils.netlifyRequest(f'/api/v1/{user}/sites', json=payload)

if(response.ok):
    print("New server was correctly created")
    print("New server ID = " + response.json()['id'])
else:
    print("There was an error:")
    print(response.status_code + " : " + response.reason)