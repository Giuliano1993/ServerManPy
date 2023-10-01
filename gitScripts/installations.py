import requests
import sys
sys.path.append("")
import utils


def getInstallations():
    user = utils.getConfig("gitUser")
    gitToken = utils.getConfig('gitToken')
    url = f"https://api.github.com/installation/repositories"

    payload={
        "readonly":True
    }
    response = requests.post(
        url=url,
        headers={
            "Accept":"application/vnd.github+json",
            "Authorization": f"Bearer {gitToken}",
            "X-GitHub-Api-Version": "2022-11-28"
        },
        json=payload
    )

    return response.json()
