"""
Program that scrapes http://leagueoflegends.wikia.com/wiki/List_of_champions
for a list of champion links, adds them to an array, and returns them.

May 2018
"""
__author__ = "Joshua Schenk"

import requests
import html5lib
from bs4 import BeautifulSoup

def getChamps():
	source = 'http://leagueoflegends.wikia.com/wiki/List_of_champions'
	html = requests.get(source)
	champSoup = BeautifulSoup(html.text, 'html5lib')
	champTable = champSoup.find('table', class_='wikitable sortable')
	champList = champTable.find("tbody")
	for tr in champList.find_all('tr'):
		champData = tr.find('a')
		print(champData.get('href'))
		

getChamps()