#!/usr/bin/env python3
# python modules
import os
import inquirer
import paramiko
import time
import webbrowser
#myModules

import dropletManager

from createWebsite import createWebsite
from utils import getConfig
questions = [
  inquirer.Text('machineName', message="Pick a name for your machine"),  
]


answers = inquirer.prompt(questions)
machineName = answers['machineName']

sizes = dropletManager.getSizes()

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

images = dropletManager.getDistributions(answers['dropletDistribution'])
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

newDroplet  = dropletManager.createDroplet(machineName,dropletSize,dropletImage)


newDroplet = dropletManager.getDroplet(newDroplet['id'])
print('[*] Creating the droplet... ', end='', flush=True)
while newDroplet['status'] != 'active' :
  newDroplet = dropletManager.getDroplet(newDroplet['id'])
  #print('.')
  time.sleep(1)
  
print('OK')
print('[*] Powering the new droplet on...', end='', flush=True)
time.sleep(60)  
print('Droplet ready')

print('[*] Connecting via SSH...', end='', flush=True)
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ip = newDroplet['networks']['v4'][0]['ip_address']
#path = os.path.expanduser('~')+'/.ssh/id_rsa_do'      
path = getConfig('localKeyFile')
ssh.connect(ip, username='root',key_filename=path)

print('CONNECTED')
commands = [
        "apt-get update",
        "apt-get install -y apache2",
        "apt-get install -y php libapache2-mod-php",
        "systemctl restart apache2",
        "php -r \"copy('https://getcomposer.org/installer', 'composer-setup.php');\"",
        "php composer-setup.php --install-dir=/usr/local/bin --filename=composer",
        "php -r \"unlink('composer-setup.php');\""
        "apt-get install -y git",
    ]
for command in commands: 
  ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
  print(ssh_stdout.read().decode())
  
ssh_stdin.close()
continueQuestion = [
  inquirer.Confirm('createWebsite', message="Do you want to create a website right now on your server?", default=True)
]

answers = inquirer.prompt(continueQuestion)
if(answers['createWebsite']):
  createWebsite(ip)
print(f"New machine is at IP: {ip}")
webbrowser.open(f'http://{ip}')
os.system(f"ssh -o StrictHostKeyChecking=no root@{ip}")



