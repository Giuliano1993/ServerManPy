import requests
from utils import buildBasicHeaders, printFormattedInfo, getConfig
from colorama import Style
import yaml

#print(response.json())

def createDroplet(name, size, image):
  headers = buildBasicHeaders()
  get_droplets_url = "https://api.digitalocean.com/v2/droplets"
  keys = getConfig('sshKeys')
  
  data = {
    'name':name,
    'size':size,
    'image':int(image),
    'ssh_keys': keys
  }
  response = requests.post(get_droplets_url, headers=headers,json=data)
  
  print(response.json())
  return response.json()['droplet']


def getDroplet(dropletId):
  headers = buildBasicHeaders()
  get_droplets_url = f"https://api.digitalocean.com/v2/droplets/{dropletId}"

  response = requests.get(get_droplets_url, headers=headers)
  return response.json()['droplet']


def getDroplets():
  headers = buildBasicHeaders()
  get_droplets_url = "https://api.digitalocean.com/v2/droplets?page=1"

  response = requests.get(get_droplets_url, headers=headers)
  return response.json()['droplets']


def getDistributions(distribution=""):
  url = f"https://api.digitalocean.com/v2/images?type=distribution"
  headers = buildBasicHeaders()

  response = requests.get(url,headers=headers)
  images = response.json()['images']
  if(distribution != ''):
    images = list(filter(lambda i: i['distribution'] == distribution.title(), images))
  images = list(filter(lambda i: i['status'] == 'available', images))
  return images


def getSshKeys():
  url = "https://api.digitalocean.com/v2/account/keys"
  headers = buildBasicHeaders()
  response = requests.get(url,headers=headers)
  return response.json()['ssh_keys']

def getSizes():
  url = "https://api.digitalocean.com/v2/sizes"
  headers = buildBasicHeaders()
  response = requests.get(url,headers=headers)
  return response.json()['sizes']
