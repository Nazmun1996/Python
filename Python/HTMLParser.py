#A Python Program to Get the links in a web page

import urllib

#This statement can change accordiing to version of Beautiful Soup
from bs4 import BeautifulSoup

#Input any URL. For Example:www.goal.com/en
url = raw_input("Enter URL:")
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')
for tag in tags:
    #Print the links(href tags)
    print tag.get('href',None)
