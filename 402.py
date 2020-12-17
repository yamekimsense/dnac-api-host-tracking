#works
#code from DNAc API
#time fixed
#get the detail of client

import http.client
import ssl
import json
import requests
from requests.auth import HTTPBasicAuth
import time

#from dnac_config import DNAC, DNAC_PORT, DNAC_USER, DNAC_PASSWORD
url = 'https://10.72.78.17/dna/system/api/v1/auth/token'
resp = requests.post(url, auth=HTTPBasicAuth("admin", "C1sco12345"), verify=False)
#print (resp)
token = resp.json()['Token']
#print("Token Retrieved: {}".format(token))


#main
conn = http.client.HTTPSConnection("10.72.78.17", context = ssl._create_unverified_context())

headers = {
    'x-auth-token': token,
    'content-type': 'application/json'
    }

starttime = 1607724000000
mac = "00:06:F6:2B:88:55"

while starttime < 1607767200001:
    timestamp = time.ctime(starttime)
    query = "/dna/intent/api/v1/client-detail?timestamp=" + str(starttime) + "&macAddress=" + mac
    conn.request("GET", query, headers=headers)
    res = conn.getresponse()
    data = res.read()
    realdata = json.loads(data.decode("utf-8"))
    #print (json.dumps(realdata, indent=8))
    apname = realdata['detail']['clientConnection']

    printtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(starttime/1000))
    print (starttime, printtime, mac, apname)
    starttime = starttime + 900000
