
import time
import netlifyUtils
import inquirer
#from ../../ import utilities.utils
import sys
sys.path.append("")		# fixes import issues

import utils

response = netlifyUtils.netlifyRequest('/api/v1/sites', method='GET')
if(response.ok):
    for site in filter(lambda s: s['published_deploy'] is not None, response.json()):
        print(f"{site['name']} : {site['url']} ")
else:
    print("There was an error:")
    print(str(response.status_code) + " : " + response.reason)
    print(response.json())