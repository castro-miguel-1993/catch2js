import urllib.request
from urllib.request import urlopen, Request
import os
import sys
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

try:
	req = Request(url=sys.argv[1], headers=headers)
	datos = urllib.request.urlopen(req).read().decode()

	file = open("./"+sys.argv[2]+".txt", "w")
	file.write("FILES .JS OF  SITE: "+sys.argv[1]+ os.linesep+ os.linesep)

	soup = BeautifulSoup(datos,features="html.parser")
	tags = soup('script')
	for tag in tags:
		if tag.get('src'):
			file.write(tag.get('src') + os.linesep)
	print("Successfully completed")
	file.close()
except:
	print("ERROR: can't get files, check its parameters or contact the developer.")
