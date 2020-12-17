#works
#code from DNAc API

import http.client
import ssl
import json
import requests
from requests.auth import HTTPBasicAuth
import time

#from dnac_config import DNAC, DNAC_PORT, DNAC_USER, DNAC_PASSWORD
url = 'https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token'
resp = requests.post(url, auth=HTTPBasicAuth("devnetuser", "Cisco123!"), verify=False)
#print (resp)
token = resp.json()['Token']
#print("Token Retrieved: {}".format(token))


#main
conn = http.client.HTTPSConnection("sandboxdnac2.cisco.com", context = ssl._create_unverified_context())

headers = {
    'x-auth-token': token,
    'content-type': 'application/json'
    }


#loop
starttime = 1607724000000

while starttime < 1607767200001:
    timestamp = time.ctime(starttime)
    starttime = starttime + 900

    timex = "1607677380000"
    mac = "00:00:2A:01:00:3F"
    query = "/dna/intent/api/v1/client-detail?timestamp=" + str(starttime) + "&macAddress=" + mac
    #query = "/dna/intent/api/v1/client-detail?timestamp=" + timex + "&macAddress=" + mac
    conn.request("GET", query, headers=headers)
    res = conn.getresponse()
    data = res.read()
    realdata = json.loads(data.decode("utf-8"))
    print (realdata)
    apname = realdata['detail']['clientConnection']
    print (timestamp, mac, apname)
