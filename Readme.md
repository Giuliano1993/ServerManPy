# doManager
This repo will contain some scripts to easily create, run and manage your server on digital ocean.
Will create a running server for your webapp in just few steps from your local terminal, make it easy for you to go over some repetetive tasks

### Instructions
In order to get this tool running, you will need some config.
- first of all you will need a Digital Ocean Token. You can get it [here](https://cloud.digitalocean.com/account/api/tokens?i=75bc4f)
- generate your key and copy it in your **env.yaml** file using in the ```doAuthToken```

#### Now add the SSH key
You can either use an already exsisting key or creating a new one.
To add a new ssh key from your computer to ssh you can go [here](https://cloud.digitalocean.com/account/security?i=75bc4f)
after adding it copy the fingerprint and add it to sshKeys in your .env file. This will allow the script to access the ssh and configure your server