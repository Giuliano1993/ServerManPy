import inquirer
from rich.console import Console
import subprocess
from rich.markdown import Markdown
console = Console()
MD = """
# Welcome to Serverman
"""
mdCOnv = Markdown(MD)
console.print(mdCOnv)
console.print("Wellcome to ServerMan, your Command Line Interface to interact with all your servers outh there", style="green")
console.print("I'm working on a Native App with GUI too for this tool", style="green")
mdLine = Markdown("""
---
""")
console.print(mdLine)

console.print("If you like this and would love to support me, you can do it on Buy me a coffee :coffee:", style="yellow")
console.print("https://www.buymeacoffee.com/ghostylab", style="bold")
console.print(mdLine)


availableCommands = [
    'Create Server',
    'Connect to server with SSH',
    'Setup Website on a server',
    'Exit'
]


question = [inquirer.List('command',message="What would you like to do?", choices=availableCommands)]
answers = inquirer.prompt(question)
commandIndex = availableCommands.index(answers['command'])

match commandIndex:
    case 0:
        subprocess.run(["python","setupServer.py"])
    case 1:
        subprocess.run(["python","connectToServer.py"])
    case 2:
        subprocess.run(["python","addWebsite.py"])
    case 3:
        exit()