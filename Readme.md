# ServerManPy
## Previously doManager
This is a tool born to easily manage servers on digital ocean platform but is on the road to become a command line tool to manage your server and website across multiple platforms.
While this is going to be open source, I'm also building a graphic interface version of this that I'll release asap.

As for its story at the moment this contains mostly Digital Ocean functionalities, but you are welcome to add your part to make this a complete Server Manager

Actually working on completing some Digital Ocean functionalities and adding connection for Netlify and Vercel
### Basic code explanation
The code from the file setupServer.py is explained in an article on [this link](https://dev.to/giuliano1993/api-ssh-create-and-setup-a-server-with-python-and-digital-ocean-58e2)

### Instructions
In order to get this tool running, you will need some config.
- first of all you will need a Digital Ocean Token. You can get it [here](https://cloud.digitalocean.com/account/api/tokens?i=75bc4f)
- generate your key and copy it in your **env.yaml** file using in the ```doAuthToken```

#### Now add the SSH key
You can either use an already exsisting key or creating a new one.
To add a new ssh key from your computer to ssh you can go [here](https://cloud.digitalocean.com/account/security?i=75bc4f)
after adding it copy the fingerprint and add it to sshKeys in your .env file. This will allow the script to access the ssh and configure your server

#### Adding git credential to your env file
In order to clone your git repositories you will need your username and token in your env file or directly prompted during server setup. Either if you want to put it in your  env file or ask for it during setup. you will need a github token in order to cone it.
You can get one by going [here](https://github.com/settings/tokens), or guided step by step: 
1. open [Github](https://github.com/)
2. click on your profile image on top right corner
3. Select "**Settings**"
4. Select "**Developer Settings**"
5. Go to Personal Access tokens > tokens
6. Generate new token
7. Choose an expiration date and check all the repo checkbokes
8. give it a name and copy your new token


#### Todos

- [ add ] delete droplet
- [ add ] remove website
- [ complete ] add website
  - can pick a configuration for a site
  - define a pipeline for the uploaded website

