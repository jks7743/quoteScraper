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
from bs4 import BeautifulSoup