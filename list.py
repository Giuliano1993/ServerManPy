import requests
from utils import buildBasicHeaders

headers = buildBasicHeaders()
get_droplets_url = "https://api.digitalocean.com/v2/droplets?page=1"

response = requests.get(get_droplets_url, headers=headers)
droplets = (response.json())['droplets']
for droplet in droplets:
    print(f"Droplet {droplet['name']} id: {droplet['id']}")
