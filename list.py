import requests
from utils import buildBasicHeaders,printFormattedInfo
from colorama import Style

headers = buildBasicHeaders()
get_droplets_url = "https://api.digitalocean.com/v2/droplets?page=1"

response = requests.get(get_droplets_url, headers=headers)
droplets = (response.json())['droplets']
for droplet in droplets:
    printFormattedInfo(droplet, 'name')
    printFormattedInfo(droplet, 'id')
    print('\n\n')

print(Style.RESET_ALL)
