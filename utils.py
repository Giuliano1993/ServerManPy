import yaml
import paramiko
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


def createSshConnection(ip):
  ssh = paramiko.SSHClient()
  ssh.load_system_host_keys()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  path = getConfig('localKeyFile')
  if(path == '' or path is None):
    path = input('Please enter yout SSH Key file path')
  ssh.connect(ip, username='root',key_filename=path)
  return ssh
  