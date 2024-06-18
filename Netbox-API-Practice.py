import requests 
import urllib3 
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
apitoken = ''
url = "https://netbox.csnt.princegeorge.ca/api/dcim/devices/"

headers = {
    'Content-Type': 'application/json',
    'Authorization': apitoken
}
response = requests.get(url, headers=headers, verify=False)
json_data = response.json()
results = json_data['results']

for device in results:
    if device['primary_ip'] is None:
        pass
    else:
        device['device_role']['slug'] == 'access-switch'
        hostname = device['name']
        ipaddr = device['primary_ip']['address']
        print('The IP address of access switch', hostname, 'is', ipaddr)