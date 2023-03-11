import requests
from utils import buildBasicHeaders, printFormattedInfo
from colorama import Style

headers = buildBasicHeaders()
get_droplets_url = "https://api.digitalocean.com/v2/droplets"
data = {
  'name':'macchinaTest',
  'size':'s-1vcpu-512mb-10gb',
  'image':112929454,
  'ssh_keys': [25525079]
}
#print(data)
response = requests.post(get_droplets_url, headers=headers,json=data)
print(response.json())
