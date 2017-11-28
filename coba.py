import os
import urllib3


http = urllib3.PoolManager()
r = http.request('GET', 'http://httpbin.org/robots.txt')
print(r)


mute='nircmd.exe mutesysvolume 1'
unmute='nircmd.exe mutesysvolume 0'



os.system('"C:/Windows/System32/notepad.exe"')
os.system('"D:/automute/nircmd.exe nircmd.exe mutesysvolume 1"'  )
