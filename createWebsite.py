import inquirer
import paramiko
import dropletManager
import os
import utils

#ask for informations like:
#   uri
#   folderName ( if different from uri ) 
#   website type [ static, wordpress, laravel ]
#   empty or from git repositoty. IF FROM GIT
#   ask for url, user, password [ can be asked or put in the env]

''' 
droplets = dropletManager.getDroplets()
dropletsChoices = []
for i, droplet in enumerate(droplets,start=1):
  choice = f"[{i}] {droplet['name']}"
  dropletsChoices.append(choice)
  
askDroplet = [ inquirer.List('dropletImage',
                message="What OS do you prefer?",
                choices=dropletsChoices,
            )]
chooseDroplet = inquirer.prompt(askDroplet)

droplet = chooseDroplet['dropletImage']
idChiusura = droplet.find(']')
index = droplet[1:idChiusura]
droplet = int(droplets[int(index)-1]['id']) '''

def createWebsite(ip):
  questions = [
    inquirer.Text('siteName', message="Pick a name for your site"),  
    inquirer.Text('folderName', message="choose a folder name, [if you wish it different from your site name]", default=''),
    inquirer.Confirm('gitRepo', message="Do you want to use a git Repo?", default=True)
  ]
  answers = inquirer.prompt(questions)
  siteName = answers['siteName']
  folderName = answers['folderName'] if answers['folderName'] != '' else answers['siteName']
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
    repoName = answers['repoName'];
    
    if(gitUser == '' or gitUser is None): 
      gitUser = answers['gitUser'];
    if(gitToken == '' or gitToken is None):
      gitToken = answers['gitToken'];
  
  
  ssh = paramiko.SSHClient()
  ssh.load_system_host_keys()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  path = os.path.expanduser('~')+'/.ssh/id_rsa_do'         
  ssh.connect(ip, username='root',key_filename=path)

  print('Connected to the server')
  commands = [
    f"cd /var/www; mkdir {folderName}; cd {folderName}; pwd",
  ]
  if(gitRepo):
    commands.append(f'cd /var/www/{folderName}; git clone https://{gitUser}:{gitToken}@github.com/{gitUser}/{repoName}.git .')
  else:
    commands.append("touch index.html")
    commands.append('echo -e "<h1>Hello World<h1>" >> index.html')
    
  
  
  for command in commands: 
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
    print(ssh_stdout.read().decode())
    if(ssh_stderr):
      print(ssh_stderr.read().decode())
    
  ssh_stdin.close()