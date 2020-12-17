#don't work

#code from DNAc platform - Dev - API
#//'x-auth-token': 'x-auth-token-value'
# //'content-type': 'application/json'
import http.client

conn = http.client.HTTPSConnection("dcloud-dna-center-inst-sjc.cisco.com")

headers = {
    'content-type': "application/json",
    'authorization': "<Authorization>"
    }

conn.request("POST", "/dna/system/api/v1/auth/token", headers=headers, auth=('demo', 'demo1234!'))

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))