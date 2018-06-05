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
league of legends wikia page
http://leagueoflegends.wikia.com/wiki/List_of_champions

:return: 
	a list of dictionaries that are internal representations of champions
		dict:
			str Name : 'champ_name'
			str Link : 'champ_link'
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
	champList = champ_table.find('tbody')
	for tr in champList.find_all('tr'):
		champ_dict = {}
		champ_data = tr.find('a')
		page_link = str(champ_data.get('href'))
		champ_dict['Name'] = page_link.rsplit('/')[2]	# get a link formated version of a champions name
		champ_links.append(champ_dict)
		champ_dict['Link'] = 'http://leagueoflegends.wikia.com' + page_link	# format link
	del champ_links[0]	# delete unnecessary link due to table formating
	for champ in champ_links:
		champ['Image'] = get_champ_image(champ)
		champ['Quotes'] = get_champ_quotes(champ)	# get champ quotes
		champ['PrettyName'] = get_pretty_name(champ)
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
		if champ_quote[0] is '"':	# filter out non-quote or noise lines
			champ_quotes.append(champ_quote)	# add quote to array
	return champ_quotes

"""
Finds a link to the image of a champion based on a given dictionary

:param champ_dict: a dictionary entry of a champion
:return: link to the image of a champion
"""
def get_champ_image(champ_dict):
	print(champ_dict['Name'])
	champ_image_link = 'http://leagueoflegends.wikia.com/wiki' + '/File:' + champ_dict['Name'] + '_OriginalSkin.jpg'
	html = requests.get(champ_image_link)
	soup = BeautifulSoup(html.text, 'html5lib')
	image_parent = soup.find('div', class_='fullImageLink')
	image_link = image_parent.find('a')
	image = image_link.get('href')
	return image

"""
Small helper function that replaces underscores and %27 with space and '
characters and returns the pretty string

:param champ_dict: a dictionary entry of a champion
:return: a pretty version of a champions name
"""
def get_pretty_name(champ_dict):
	champ_name = str(champ_dict['Name'])
	pretty_name = champ_name.replace('_', ' ')
	pretty_name = pretty_name.replace('%27','\'')
	return pretty_name
