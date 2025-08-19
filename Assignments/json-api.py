import json, ssl
import urllib.request, urllib.parse, urllib.error

service_url = 'http://py4e-data.dr-chuck.net/opengeo?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
place =''
while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break
    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = service_url + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    try:
        js = json.loads(data)
    except:
        js = None

    print(json.dumps(js, indent=2))

    place = js['features'][0]['properties']['plus_code']
print('The place id for', address, 'is', place)


