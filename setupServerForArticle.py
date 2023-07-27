#!/usr/bin/env python3

'''
This is a simpler version off the setupServer.py script, for the article written on Dev.To
'''




# python modules
import os
import inquirer
import paramiko
import time
import webbrowser

#myModules
import dropletManager
from utils import getConfig


sizes = dropletManager.getSizes()

sizeChoices = []
for i, size in enumerate(sizes):
  choice = f"[{i+1}] RAM: {size['memory']}MB, CPUs: {size['vcpus']}, disk: {size['disk']}GB"
  sizeChoices.append(choice)

images = dropletManager.getDistributions()
imageChoices = []
for i,image in enumerate(images):
  choice = f"[{i+1}] {image['description']}"
  imageChoices.append(choice)
  

questions = [
  inquirer.Text('machineName', message="Pick a name for your machine"),  
  inquirer.List('dropletSize', message="What size do you need?", choices=sizeChoices ),
  inquirer.List('dropletImage', message="What OS do you prefer?", choices=imageChoices)
]

answers = inquirer.prompt(questions)

machineName = answers['machineName']
  
index = sizeChoices.index(answers['dropletSize'])
dropletSize = sizes[index]['slug']

index = imageChoices.index(answers['dropletImage'])
dropletImage = images[index]['id']

newDroplet  = dropletManager.createDroplet(machineName,dropletSize,dropletImage)


newDroplet = dropletManager.getDroplet(newDroplet['id'])
print('[*] Creating the droplet... ', end='', flush=True)
while newDroplet['status'] != 'active' :
  newDroplet = dropletManager.getDroplet(newDroplet['id'])
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
path = getConfig('localKeyFile')
ssh.connect(ip, username='root',key_filename=path)

print('CONNECTED')
commands = [
        "apt-get update",
        "apt-get install -y apache2",
        # add all the commands you'd like to exec
    ]
for command in commands: 
  ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
  print(ssh_stdout.read().decode())
  
ssh_stdin.close()

print(f"New machine is at IP: {ip}")
webbrowser.open(f'http://{ip}')
os.system(f"ssh -o StrictHostKeyChecking=no root@{ip}")



