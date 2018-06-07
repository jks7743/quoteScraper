# quote_scraper
This is a web-scraper application for future use in [OKrammus](https://github.com/htmercury/OKrammus). This python script scrapes the [League of Legends wikia](http://leagueoflegends.wikia.com/wiki/Wiki) for champion information and builds a list of dictionaries with the following format

champ_dict:
	str Name : 'champ_name'
	str Link : 'champ_Link'
	str Image : 'image_link'
	str Quotes : ['"champ quote"',...]
	str PrettyName : 'champ name'


This repo includes seperate scraper and upload scripts
* Uses python3, Beautifulsoup4, requests, html5lib, gpspread, time, and oauth2client libraries
* Requires Google Spreadsheets API credentials (this script accounts for default read and write limitations)

## Getting Started
//TODO

## Planned Features
* Find a way to more effiecient way scrape data and update the database
* Quote filters?
