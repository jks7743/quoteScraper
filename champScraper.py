"""
Program that scrapes http://leagueoflegends.wikia.com/wiki/List_of_champions
for a list of champion links, formats them, adds them to an array
, and returns them.

May 2018
"""
__author__ = "Joshua Schenk"

import requests
import html5lib
from bs4 import BeautifulSoup

def getChamps():
	champLinks = []
	source = 'http://leagueoflegends.wikia.com/wiki/List_of_champions'
	html = requests.get(source)
	champSoup = BeautifulSoup(html.text, 'html5lib')
	champTable = champSoup.find('table', class_='wikitable sortable')
	champList = champTable.find("tbody")
	for tr in champList.find_all('tr'):
		champData = tr.find('a')
		champLinks.append('http://leagueoflegends.wikia.com' + champData.get('href'))	# format link
	del champLinks[0]	# delete unnecessary link
	return champLinks

print(getChamps())
