import inquirer
import subprocess



commands = [
    "Back",
    "Exit"
]




question = [inquirer.List('command',message="What would you like to do?", choices=commands)]
answers = inquirer.prompt(question)
commandIndex = commands.index(answers['command'])

match commandIndex:
    case 0:
        subprocess.run(['python',"serverMan.py"])
    case 1:
        exit()