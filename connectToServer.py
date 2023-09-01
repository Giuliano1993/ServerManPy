import inquirer
import os
import dropletManager
import paramiko
from createWebsite import createWebsite
from utils import getConfig

droplets = dropletManager.getDroplets()
dropChoices = []
for i, droplet in enumerate(droplets):
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

os.system(f"ssh -o StrictHostKeyChecking=no root@{ip}")