#!/usr/bin/env python3
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

json = ServiceAccountCredentials.from_json_keyfile_name('twitter form test-7fb01488db9e.json', scope)

gc = gspread.authorize(json)

sheet = gc.open('ツイート内容リクエストフォーム（回答）').sheet1

print(sheet.acell('A1'))
