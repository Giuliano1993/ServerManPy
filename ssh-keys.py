import requests
from utils import buildBasicHeaders, printFormattedInfo
from colorama import Style

headers = buildBasicHeaders()
get_droplets_url = "https://api.digitalocean.com/v2/account/keys"

response = requests.get(get_droplets_url, headers=headers)
keys = response.json()['ssh_keys'] 
for key in keys:
  printFormattedInfo(key, 'id')
  printFormattedInfo(key, 'name')
  
  print('\n\n')
print(Style.RESET_ALL)