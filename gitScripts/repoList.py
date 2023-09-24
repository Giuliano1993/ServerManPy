import requests
import sys
sys.path.append("")
import utils

def repoList():
    user = utils.getConfig("gitUser")
    gitToken = utils.getConfig('gitToken')
    url = f"https://api.github.com/users/{user}/repos?per_page=100"

    response = requests.get(
        url=url,
        headers={
            "Accept":"application/vnd.github+json",
            "Authorization": f"Bearer {gitToken}",
            "X-GitHub-Api-Version": "2022-11-28"
        }
    )

    return response.json()
