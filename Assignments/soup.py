import urllib.request
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
sum, count = 0, 0
tags = soup('span')
for tag in tags:
    count +=1
    sum += int(tag.contents[0])

print('Count '+ str(count) )
print('Sum ' + str(sum))