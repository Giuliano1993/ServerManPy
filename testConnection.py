import paramiko
import yaml
import os

path = os.path.expanduser('~')+'/.ssh/id_rsa_do'
configs = yaml.safe_load(open('./env.yaml'))
ip = configs['configs']['testConnectionIp']
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())                
ssh.connect(ip, username='root',key_filename=path)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ls -al")
for line in ssh_stdout:
  print(line)
ssh_stdin.close()
