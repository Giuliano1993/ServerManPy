import inquirer
import dropletManager
from createWebsite import createWebsite
droplets = dropletManager.getDroplets()
#print(droplets)
dropChoices = []
for i, droplet in enumerate(droplets):
    #print(droplet['networks']['v4'][0]['ip_address'])
    choice = f"[{i}] {droplet['name']}"
    dropChoices.append(choice)


questions = [
    inquirer.List('droplet',message="pick a droplet you wish to add a site too", choices=dropChoices)
]

answers = inquirer.prompt(questions)
dropletIndex = dropChoices.index(answers['droplet'])
droplet = droplets[dropletIndex]


print(droplet['name'])
print(droplet['networks']['v4'][0]['ip_address'])
ip = droplet['networks']['v4'][0]['ip_address']
createWebsite(ip)