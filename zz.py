#import urllib, json

#response = urllib.urlopen(url)
##print data


import os
import urllib3.request, json
with urllib3.request.urlopen("http://10.151.62.3:8081/feeder/Laboratorium+Pemrograman+2") as url:
    data = json.loads(url.read().decode())
    print(data)
