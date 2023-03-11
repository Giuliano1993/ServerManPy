import requests
import inquirer
from utils import buildBasicHeaders
from dropletDistriutions import getDistributions
from dropletSizes import getSizes
from createDroplet import createDroplet

questions = [
  inquirer.Text('machineName', message="Pick a name for your machine"),  
]

answers = inquirer.prompt(questions)
machineName = answers['machineName']

sizes = getSizes()

sizeChoices = []
for i,size in enumerate(sizes, start=1):
  choice = f"[{i}] RAM: {size['memory']}MB, CPUs: {size['vcpus']}, disk: {size['disk']}GB"
  sizeChoices.append(choice)
  
questions = [ inquirer.List('dropletSize',
                message="What size do you need?",
                choices=sizeChoices,
            )]
answers = inquirer.prompt(questions)

dropletSize = answers['dropletSize']
idChiusura = dropletSize.find(']')
index = dropletSize[1:idChiusura]

dropletSize = sizes[int(index)-1]['slug']


questions = [
  inquirer.Text('dropletDistribution', message="Specify a distribution if you wish ( for example ubuntu, debian...)"),  
]

answers = inquirer.prompt(questions)

images = getDistributions(answers['dropletDistribution'])
imageChoices = []
for i,image in enumerate(images, start=1):
  choice = f"[{i}] {image['description']}"
  imageChoices.append(choice)
  
questions = [ inquirer.List('dropletImage',
                message="What OS do you prefer?",
                choices=imageChoices,
            )]
answers = inquirer.prompt(questions)



dropletImage = answers['dropletImage']
idChiusura = dropletImage.find(']')
index = dropletImage[1:idChiusura]

dropletImage = int(images[int(index)-1]['id'])

res  = createDroplet(machineName,dropletSize,dropletImage)
print(res)


