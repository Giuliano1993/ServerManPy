import requests
import sys
import os
sys.path.append("")
import utils

def createDeployKey(repo):
    user = utils.getConfig("gitUser")
    gitToken = utils.getConfig('gitToken')
    userMail = utils.getConfig('userMail')
    if(userMail is not None):
        mailParam = f"-C {userMail}"
    else:
        mailParam = ""
    
    home_dir = os.path.expanduser("~")
    ssh_dir = os.path.join(home_dir, ".ssh")
    print("insert a name for your key")
    name = input()
    keyNamePath = ssh_dir + "\git_generated_" + name

    os.system(f'ssh-keygen -q -t ed25519 -N "" -f {keyNamePath} {mailParam}')

    with open(keyNamePath+".pub", "r") as f_in:
        key = f_in.readline()
    

    url = f"https://api.github.com/repos/{user}/{repo}/keys"

    data = {
        "title": "Deploy Key",
        "key": key,
        "read_only": True
    }
    response = requests.post(
        url=url,
        headers={
            "Accept":"application/vnd.github+json",
            "Authorization": f"Bearer {gitToken}",
            "X-GitHub-Api-Version": "2022-11-28"
        },
        json=data
    )

    return response.json()


def getDeployKeys(repo):
    user = utils.getConfig("gitUser")
    gitToken = utils.getConfig('gitToken')
    url = f"https://api.github.com/repos/{user}/{repo}/keys"

    response = requests.get(
        url=url,
        headers={
            "Accept":"application/vnd.github+json",
            "Authorization": f"Bearer {gitToken}",
            "X-GitHub-Api-Version": "2022-11-28"
        },
    )
    return response.json()