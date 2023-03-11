import requests
from colorama import Style
from utils import buildBasicHeaders, printFormattedInfo


def getSizes():
  url = "https://api.digitalocean.com/v2/sizes"
  headers = buildBasicHeaders()
  response = requests.get(url,headers=headers)
  return response.json()['sizes']


''' 
#print(response.json()['sizes'])
for size in response.json()['sizes']:
  printFormattedInfo(size, 'slug')
  printFormattedInfo(size, 'memory', text='RAM', append='MB')
  printFormattedInfo(size, 'vcpus', text = 'CPUs')
  printFormattedInfo(size, 'disk', append='GB')
  printFormattedInfo(size, 'price_monthly')
  printFormattedInfo(size, 'price_hourly')
  print('\n\n')
 
  
print(Style.RESET_ALL) '''