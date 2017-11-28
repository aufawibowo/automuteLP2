import json
import requests
import time
import os


while(1) :
	print('Scrapping data... ')

	url = "http://10.151.62.3:8081/feeder/Laboratorium%20Pemrograman%202"
	header = {'x-requested-with': 'XMLHttpRequest'}
	t = requests.get(url)
	json_data=json.loads(t.text)

	nowEvent = json_data['now'][0];

	if (nowEvent['jumlah']) :
		#print('ADA EVENT')
		os.system('"D:/automute/nircmd.exe nircmd.exe mutesysvolume 1"')
	else :
		os.system('"D:/automute/nircmd.exe nircmd.exe mutesysvolume 0"')



	time.sleep(1)
