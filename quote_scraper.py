"""
A web scraper program used to scrape
http://leagueoflegends.wikia.com/wiki/List_of_champions
for champion names, quotes and images using the BeautifulSoup4 and Requests
packages. The program outputs the information to a google spreadsheet for use
with the OKRammus API

The program creates a list of dictionaries to be uploaded to an online database
each entry has the format.
	champ_dict:
		str Name : 'champ_name'
		str Link : 'champ_Link'
		str Image : 'image_link'
		str Quotes : ['"champ quote"',...]
		str PrettyName : 'champ name'

May 2018
"""
__author__ = "Joshua Schenk"

import requests
import html5lib
from bs4 import BeautifulSoup

"""
Constructs a list of dictionaries represnting all the champions listed in the
league of legendswikia page
http://leagueoflegends.wikia.com/wiki/List_of_champions

:return: 
	a list of dictionaries that are internal representations of champions
		dict:
			str Name : 'champ_name'
			str Link : 'champ_Link'
			str Image : 'image_link'
			str Quotes : ['"champ quote"',...]
			str PrettyName : 'champ name'
"""
def get_champs():
	champ_links = []
	source = 'http://leagueoflegends.wikia.com/wiki/List_of_champions'
	html = requests.get(source)
	champ_soup = BeautifulSoup(html.text, 'html5lib')
	champ_table = champ_soup.find('table', class_='wikitable sortable')	# find the right table
	champList = champ_table.find("tbody")
	for tr in champList.find_all('tr'):
		champ_dict = {}
		champ_data = tr.find('a')
		page_link = str(champ_data.get('href'))
		champ_dict['Name'] = page_link.rsplit('/')[2]	# get a link formated version of a champions name
		champ_links.append(champ_dict)
		champ_dict['Link'] = 'http://leagueoflegends.wikia.com' + page_link	# format link
		# champ_dict['Quotes'] = get_champ_quotes(champ_dict['Link'])	# get champ quotes
	del champ_links[0]	# delete unnecessary link due to table formating
	return champ_links

"""
Function finds and returns a list of all the quotes a champion has based on a
given wikia link

:param champ_dict: a dictionary entry of a champion
:return: a list of champion quotes
"""
def get_champ_quotes(champ_dict):
	champ_quotes = []
	champ_link = champ_dict['Link']	# get a champ's link
	html = requests.get(champ_link + '/Quotes')	# go to Quote page for easy parsing
	soup = BeautifulSoup(html.text, 'html5lib')
	for i in soup.find_all('i'):
		champ_quote = str(i.string)	# make thee quote a string
		if champ_quote[0] is '"':	# remove non-quote or noise lines
			champ_quotes.append(champ_quote)	# add quote to array
	return champ_quotes

print(get_champs())

"""
Finds a link to the image of a champion based on a given link

:param champ_link: a link to a champions wikia page
:return: link to the image of a champion
"""
# def getChampImage(champ_link):
	
