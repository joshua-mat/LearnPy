import json, ssl
from urllib.request import urlopen

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL ')
print('Retrieving', url)
response = urlopen(url, context=ctx)
data_json = json.loads(response.read())
print('Retrieved',len(data_json),'characters')
json_sum, count = 0, 0

for item in data_json['comments']:
    num = int(item['count'])
    json_sum += num
    count += 1

print('Count',count)
print('Sum',json_sum)