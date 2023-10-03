
import time
import netlifyUtils
import inquirer
#from ../../ import utilities.utils
import sys
sys.path.append("")		# fixes import issues

import utils
from gitScripts import repoList, getDeployKey




def chooseRepo():
    repos = repoList.repoList()
    
    repoChoices = []
    for i, repo in enumerate(repos):
        choice = repo['full_name']
        repoChoices.append(choice)

    chooseRepo = [inquirer.List('pickRepo', message="choose a repo you want to link to the site", choices=repoChoices)]
    answers = inquirer.prompt(chooseRepo)
    index = repoChoices.index(answers['pickRepo'])
    return repos[index]

#https://answers.netlify.com/t/deploy-the-github-repo-using-api/24269/13    
#check the bottom line here can find some usegful insight of how get this going, maybe
#keep tryingbebtter and more focused
#https://docs.github.com/en/rest/deploy-keys/deploy-keys?apiVersion=2022-11-28#about-deploy-keys
#https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys
# bash script that generates deploy key
#https://gist.github.com/noah/3ed929858802a474eeff888c9d3a2ac9

#this was the final thing missing: you need the netlify installation id 
#https://answers.netlify.com/t/unable-to-deploy-a-private-repo-using-the-api/81869/9

installationId = utils.getConfig("githubTestInstallationId")



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
    repo = chooseRepo()
    pk = netlifyUtils.getDeployKey()
    depKey = getDeployKey.getDeployKeys(repo['name'])
    if(len(depKey) == 0):
        depKey = getDeployKey.createDeployKey(repo['name'])
    else:
        depKey = depKey[0] 
    payload['repo'] = {
        "branch": repo['default_branch'],
        "cmd": "npm run build",
        "deploy_key_id": depKey['id'],
        "dir": "dist/",
        "private": False,
        "provider": "github",
        "repo": repo['full_name'],
        "repo_id": repo['id'],
        "installation_id": installationId
    }
    payload["build_settings"] = payload['repo']

response = netlifyUtils.netlifyRequest(f'/api/v1/{user}/sites', json=payload)

if(response.ok):
    print("New server was correctly created")
    print("New server ID = " + response.json()['id'])
else:
    print("There was an error:")
    print(str(response.status_code) + " : " + response.reason)
    print(response.json())

