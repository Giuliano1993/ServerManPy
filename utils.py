import yaml
#response = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
#print(response.json())


def buildBasicHeaders():
  configs = yaml.safe_load(open('./env.yaml'))
  token = configs['configs']['doAuthToken']
  headers = {'Content-Type':'application/json','Authorization':'Bearer '+token}
  return headers