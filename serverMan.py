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
console.print("Welcome to ServerMan, your Command Line Interface to interact with all your servers outh there", style="green")
console.print("I'm working on a Native App with GUI too for this tool", style="green")
mdLine = Markdown("""
---
""")
console.print(mdLine)

console.print("If you like this and would love to support me, you can do it on Buy me a coffee :coffee:", style="yellow")
console.print("https://www.buymeacoffee.com/ghostylab", style="bold")
console.print(mdLine)


console.print("What platform want to use?")

platforms = ["Digital Ocean","Netlify","Vercel","Exit"]
question = [inquirer.List('command',message="What would you like to do?", choices=platforms)]
answers = inquirer.prompt(question)
commandIndex = platforms.index(answers['command'])

if(answers['command'] == 'Exit'):exit()
spacecleanPlatform = answers['command'].replace(" ","")
folder = spacecleanPlatform[0].lower() + spacecleanPlatform[1:]
commandListPath = './platforms/'+folder+'/commands.py'
subprocess.run(["python", commandListPath])



