#works
#to get the token

import http.client
import ssl

conn = http.client.HTTPSConnection("10.72.78.17", context = ssl._create_unverified_context())

headers = { 'authorization': "Basic YWRtaW46QzFzY28xMjM0NQ==" }

conn.request("POST", "/dna/system/api/v1/auth/token", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))