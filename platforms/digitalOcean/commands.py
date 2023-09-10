import inquirer
import subprocess



commands = [
    'Create Server',
    'Connect to server with SSH',
    'Setup Website on a server',
    "Back",
    'Exit'
]


question = [inquirer.List('command',message="What would you like to do?", choices=commands)]
answers = inquirer.prompt(question)
commandIndex = commands.index(answers['command'])

match commandIndex:
    case 0:
        subprocess.run(["python","setupServer.py"])
    case 1:
        subprocess.run(["python","connectToServer.py"])
    case 2:
        subprocess.run(["python","addWebsite.py"])
    case 3:
        subprocess.run(['python',"serverMan.py"])
    case 4:
        exit()