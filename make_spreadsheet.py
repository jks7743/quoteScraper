"""
Small script that uploads quotes scraped by quote_scraper.py to a google spreadsheet named
League Quotes. This requires the use of the Google Drive API and a .json file named
client_secret.json with the credentials to run.

June 2018
"""
__author__ = "Joshua Schenk"

import gspread
import time
from quote_scraper import get_champs
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
		'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)

quote_sheet = client.open("League Quotes").sheet1

champ_list = get_champs()
index = 2

for champ in champ_list:
	row = [ champ['Name'], champ['Link'], champ['Image'], ','.join(champ['Quotes']), champ['PrettyName'] ]
	quote_sheet.insert_row(row, index)
	time.sleep(6)
	index += 1
