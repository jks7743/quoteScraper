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

# for champ in champ_list: