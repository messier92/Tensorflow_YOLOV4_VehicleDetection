# TO RUN ON PYTHON 3.7 ONLY #
import requests
import json
from bs4 import BeautifulSoup
from collections import Counter
import os
import PIL
import urllib
import sys
from urllib.request import urlretrieve
from urllib.request import urlopen, Request

# Perform GET request
url = "https://api.data.gov.sg/v1/transport/traffic-images"
response = requests.get(url)

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    # print(text)

# Check the full json
jprint(response.json())

imageurllist = []

camera_items = response.json()['items']

json_data = json.dumps(camera_items)
numberofimages = json_data.count('image')

try:
    for d in camera_items:
        for i in range(numberofimages):
            imageurl = d['cameras'][i]['image']
            imageurllist.append(imageurl)

except:
    print("End of JSON")


file_path = "D:\ImageRec\sgmy_traffic_images"
opener = urllib.request.URLopener()
opener.addheader('User-Agent', 'Mozilla/5.0')

for j, url in enumerate(imageurllist):
    # for naming convention - +1261 to the previous number
    j += 1858
    filename = 'imgs_{}.jpg'.format(j)
    full_path = '{}{}'.format(file_path, filename)
    opener.retrieve(url, filename)

    print('{} saved at {}.'.format(filename, file_path))

input('Press ENTER to exit')
