import yaml
from colorama import Fore, Back, Style


def buildBasicHeaders():
  token = getConfig('doAuthToken')
  headers = {'Content-Type':'application/json','Authorization':'Bearer '+token}
  return headers


def printFormattedInfo(obj, property, text = '', append = ''):
  if(text == ''): text = property
  print(Fore.WHITE + f'- {text}: ' + Fore.RED + str(obj[property]) + append)
  

def getConfig(configName):
  configsFile = yaml.safe_load(open('./env.yaml'))
  return configsFile['configs'][configName]
  