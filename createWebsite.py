import inquirer
import paramiko
from scp import SCPClient, SCPException
import os
import utils
import sys
import socket

#ask for informations like:
#   uri
#   folderName ( if different from uri ) 
#   website type [ static, wordpress, laravel ]
#   empty or from git repositoty. IF FROM GIT
#   ask for url, user, password [ can be asked or put in the env]

def createWebsite(ip):
  questions = [
    inquirer.Text('siteName', message="Pick a name for your site"),  
    inquirer.Text('folderName', message="choose a folder name, [if you wish it different from your site name]", default=''),
    inquirer.Confirm('gitRepo', message="Do you want to use gitRepoa git Repo?", default=True)
  ]
  answers = inquirer.prompt(questions)
  siteName = answers['siteName'].replace(' ','-')
  folderName = answers['folderName'].replace(' ','-') if answers['folderName'] != '' else answers['siteName'].replace(' ','-')
  gitRepo = answers['gitRepo']

  print(siteName)
  print(folderName)
  print(gitRepo)

  if(gitRepo):
    gitUser = utils.getConfig('gitUser')
    gitToken = utils.getConfig('gitToken')
    questions = [
      inquirer.Text('repoName', message="type your repository name")
    ]
    if(gitUser == '' or gitUser is None): 
      questions.append(inquirer.Text('gitUser', message="type your git username here"))
      
    if(gitToken == '' or gitToken is None):
      inquirer.Text('gitToken', message="type your git password here"),   
    answers = inquirer.prompt(questions)
    repoName = answers['repoName']
    
    if(gitUser == '' or gitUser is None): 
      gitUser = answers['gitUser']
    if(gitToken == '' or gitToken is None):
      gitToken = answers['gitToken']
  
  try:
    ssh = utils.createSshConnection(ip)
  except paramiko.BadHostKeyException as e:
    print('Server Host Key could not be verified')
    sys.exit(1)
  except paramiko.AuthenticationException as e:
    print('Authentication failed')
    sys.exit(1)
  except socket.error as e:
    print('Socket error: %s',e.message )
    sys.exit(1)
  except Exception as e:
    print(e.message)
    sys.exit(1)
    
    
  print('Connected to the server')
  commands = [
    f"cd /var/www; mkdir {folderName}; cd {folderName}; pwd",
  ]
  if(gitRepo):
    commands.append(f'cd /var/www/{folderName}; git clone https://{gitUser}:{gitToken}@github.com/{gitUser}/{repoName}.git .')
  else:
    commands.append(f"touch /var/www/{folderName}/index.html")
    commands.append(f'echo -e "<h1>Hello World {folderName}<h1>" >> /var/www/{folderName}/index.html')
    
  
  
  for command in commands: 
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
    print( f"[Running] - {command}")
    print(ssh_stdout.read().decode())
    if(ssh_stderr):
      print(ssh_stderr.read().decode())
    
    
  try:
    scpClient = SCPClient(ssh.get_transport())
    confName = siteName.split(".")[0]+".conf"
    scpClient.put('./confs/apache/defaultDomain.conf',remote_path=f'/etc/apache2/sites-available/{confName}')
  except SCPException as e:
    print(e)
  except Exception as e:
    print(e)
    
  enableSiteCommands = [
    f"sed -i 's/SITEFOLDERNAME/{folderName}/g' /etc/apache2/sites-available/{confName}",
    f'a2ensite {confName}',
    'a2dissite 000-default.conf',
    'apache2ctl configtest'
  ]
  
  
  for command in enableSiteCommands: 
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
    print( f"[Running] - {command}")
    print(ssh_stdout.read().decode())
    if(ssh_stderr):
      print(ssh_stderr.read().decode())
      
  if(ssh_stdout.read().decode().find('Syntax OK')):
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('systemctl restart apache2')

  ssh_stdin.close()