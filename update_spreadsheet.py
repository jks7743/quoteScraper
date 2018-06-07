"""
First version of update script for faster update times due to having less writes
The script compares new data with the data in the spreadsheet to see whether a write
is required.
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
	champName = quote_sheet.cell(index, 1, value_render_option='UNFORMATTED_VALUE')
	if champName != champ['Name']:
		row = [ champ['Name'], champ['Link'], champ['Image'], ','.join(champ['Quotes']), champ['PrettyName'] ]
		quote_sheet.insert_row(row, index)
		index += 1
	else:
		champLink = quote_sheet.cell(index, 2, value_render_option='UNFORMATTED_VALUE')
		champImage = quote_sheet.cell(index, 3, value_render_option='UNFORMATTED_VALUE')
		champQuotes = quote_sheet.cell(index, 4, value_render_option='UNFORMATTED_VALUE')
		if champ['Link'] != champLink:
			quote_sheet.update_cell(index, 2, champ['Link'])
		if champ['Image'] != champImage:
			quote_sheet.update_cell(index, 3, champ['Image'])
		if ','.join(champ['Quotes']) != champQuotes:
			quote_sheet.update_cell(index, 4, ','.join(champ['Quotes']))