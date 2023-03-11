import requests
import sys
from utils import buildBasicHeaders, printFormattedInfo
from colorama import Style

headers = buildBasicHeaders()
dropletId = sys.argv[1]
get_droplets_url = f"https://api.digitalocean.com/v2/droplets/{dropletId}"

response = requests.get(get_droplets_url, headers=headers)
droplet = response.json()['droplet']

printFormattedInfo(droplet, 'id')
printFormattedInfo(droplet, 'name')
printFormattedInfo(droplet, 'status')
if(len(droplet['networks']['v4']) > 0):
  printFormattedInfo(droplet['networks']['v4'][0], 'ip_address')



print(Style.RESET_ALL)
