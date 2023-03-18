import requests
from utils import buildBasicHeaders, printFormattedInfo
from colorama import Style
import yaml

#print(response.json())

def createDroplet(name, size, image):
  headers = buildBasicHeaders()
  get_droplets_url = "https://api.digitalocean.com/v2/droplets"
  configs = yaml.safe_load(open('./env.yaml'))
  keys = configs['configs']['sshKeys']
  
  data = {
    'name':name,
    'size':size,
    'image':int(image),
    'ssh_keys': keys
  }
  #print(data)
  response = requests.post(get_droplets_url, headers=headers,json=data)
  return response.json()['droplet']


def getDroplet(dropletId):
  headers = buildBasicHeaders()
  get_droplets_url = f"https://api.digitalocean.com/v2/droplets/{dropletId}"

  response = requests.get(get_droplets_url, headers=headers)
  return response.json()['droplet']


def getDistributions(distribution=""):
  url = f"https://api.digitalocean.com/v2/images?type=distribution"
  headers = buildBasicHeaders()

  response = requests.get(url,headers=headers)
  images = response.json()['images']
  if(distribution != ''):
    images = list(filter(lambda i: i['distribution'] == distribution.title(), images))
  images = list(filter(lambda i: i['status'] == 'available', images))
  return images




def getSizes():
  url = "https://api.digitalocean.com/v2/sizes"
  headers = buildBasicHeaders()
  response = requests.get(url,headers=headers)
  return response.json()['sizes']
