import requests
import sys
sys.path.append("")
import utils

def createDeployKey(repo, publicKey):
    user = utils.getConfig("gitUser")
    gitToken = utils.getConfig('gitToken')
    url = f"https://api.github.com/repos/{user}/{repo}/keys"

    data = {
        "title": "Deploy Key",
        "key": publicKey,
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