import inquirer
import subprocess


commands = [
    "Create Site",
    "List Sites",
    "Back",
    "Exit"
]


question = [inquirer.List('command',message="What would you like to do?", choices=commands)]
answers = inquirer.prompt(question)
commandIndex = commands.index(answers['command'])

match commandIndex:
    case 0:
        subprocess.run(["python","./platforms/netlify/createServer.py"])
    case 1:
        subprocess.run(["python","./platforms/netlify/listSites.py"])
    case 2:
        subprocess.run(['python',"serverMan.py"])
    case 3:
        exit()