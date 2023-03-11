import requests
from colorama import Style
from utils import buildBasicHeaders, printFormattedInfo




def getDistributions(distribution=""):
  url = f"https://api.digitalocean.com/v2/images?type=distribution"
  headers = buildBasicHeaders()

  response = requests.get(url,headers=headers)
  images = response.json()['images']
  if(distribution != ''):
    images = list(filter(lambda i: i['distribution'] == distribution.title(), images))
  images = list(filter(lambda i: i['status'] == 'available', images))
  return images

''' 
distribution = input("please, specify a distribution (ubuntu|debian)")

images = getDistributions(distribution)
for image in images:
  printFormattedInfo(image,'id')
  printFormattedInfo(image,'slug')
  printFormattedInfo(image,'description')
  print('\n\n')
  
print(Style.RESET_ALL)

 '''