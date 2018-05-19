"""
A Web Scrapper program used to scrape
http://leagueoflegends.wikia.com/wiki/List_of_champions
for champion names, quotes and images using the BeautifulSoup4 and Requests
packages. The program outputs the information to a google spreadsheet for use
with the OKRammus API

May 2018
"""
__author__ = "Joshua Schenk"

import requests
import html5lib
from bs4 import BeautifulSoup

"""
Create a list of wiki links to all the champions listed in the league of legends
wikia page by using BeautifulSoup4 to scrape the page
http://leagueoflegends.wikia.com/wiki/List_of_champions

:return: a list of links to champion wikia pages
"""
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
