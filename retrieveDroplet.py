import requests
import sys
from utils import buildBasicHeaders, printFormattedInfo
from colorama import Style


def getDroplet(dropletId):
  headers = buildBasicHeaders()
  get_droplets_url = f"https://api.digitalocean.com/v2/droplets/{dropletId}"

  response = requests.get(get_droplets_url, headers=headers)
  return response.json()['droplet']

''' printFormattedInfo(droplet, 'id')
printFormattedInfo(droplet, 'name')
printFormattedInfo(droplet, 'status')
if(len(droplet['networks']['v4']) > 0):
  printFormattedInfo(droplet['networks']['v4'][0], 'ip_address')



print(Style.RESET_ALL) '''

