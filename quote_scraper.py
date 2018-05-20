"""
A web scraper program used to scrape
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
def get_champs():
	champ_links = []
	source = 'http://leagueoflegends.wikia.com/wiki/List_of_champions'
	html = requests.get(source)
	champ_soup = BeautifulSoup(html.text, 'html5lib')
	champ_table = champ_soup.find('table', class_='wikitable sortable')
	champList = champ_table.find("tbody")
	for tr in champList.find_all('tr'):
		champ_data = tr.find('a')
		champ_links.append('http://leagueoflegends.wikia.com' + champ_data.get('href'))	# format link
	del champ_links[0]	# delete unnecessary link
	return champ_links

"""
Function finds and returns a list of all the quotes a champion has based on a
given wikia link

:param champ_link: a link to a champions wikia page
:return: a list of champion quotes
"""
def get_champ_quotes(champ_link):
	champ_quotes = []
	html = requests.get(champ_link + '/Quotes')	# go to Quote page for easy parsing
	soup = BeautifulSoup(html.text, 'html5lib')
	for i in soup.find_all('i'):
		champ_quote = str(i.string)	# make thee quote a string
		if champ_quote[0] is '"':	# remove non-quote or noise lines
			champ_quotes.append(champ_quote)	# add quote to array
	return champ_quotes

print(get_champ_quotes('http://leagueoflegends.wikia.com/Aurelion_Sol'))
# def getChampImage(champ_link):
