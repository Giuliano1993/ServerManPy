import requests
from utils import buildBasicHeaders, printFormattedInfo
from colorama import Style


#print(response.json())

def createDroplet(name, size, image):
  headers = buildBasicHeaders()
  get_droplets_url = "https://api.digitalocean.com/v2/droplets"
  data = {
    'name':name,
    'size':size,
    'image':int(image),
    'ssh_keys': [25525079]
  }
  #print(data)
  response = requests.post(get_droplets_url, headers=headers,json=data)
  return response.json()