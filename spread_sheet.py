#!/usr/bin/env python3
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import secret
from setting import *

scope = ['https://spreadsheets.google.com/feeds']
json = ServiceAccountCredentials.from_json_keyfile_name(secret.JSON_FILE_NAME, scope)
gc = gspread.authorize(json)
sheet = gc.open_by_key(secret.SPREAD_SHEET_KEY).sheet1

def lock_sheet():
	sheet.update_cell(BOT_STATUS_ROW, BOT_STATUS_COL, BOT_STATUS_LOCK)

def unlock_sheet():
	sheet.update_cell(BOT_STATUS_ROW, BOT_STATUS_COL, BOT_STATUS_DEFAULT)

def init_status():
	i=1
	while get_timestamp(i) != "":
		if(get_status(i) == ""):
			set_status(i,STATUS_PREPARE)
		i+=1

def init():
	lock_sheet()
	init_status()

def end():
	unlock_sheet()

def get_val(num, col):
	return sheet.cell(BASE_ROW+num, BASE_COL+col).value

def set_val(num, col, val):
	sheet.update_cell(BASE_ROW+num, BASE_COL+col, val)

def get_status(num):
	return get_val(num, STATUS_COL)

def set_status(num, val):
	set_val(num, STATUS_COL, val)

def get_timestamp(num):
	return get_val(num, TIMESTAMP_COL)

def set_timestamp(num, val):
	set_val(num, TIMESTAMP_COL, val)

def get_mailaddr(num):
	return get_val(num, MAILADDR_COL)

def set_mailaddr(num):
	set_val(num, MAILADDR_COL, val)

def get_tweet_num_times(num):
	return get_val(num, TWEET_NUM_TIMES_COL)

def set_tweet_num_times(num, val):
	set_val(num, TWEET_NUM_TIMES_COL, val)

def get_tweet_day(num):
	return get_val(num, TWEET_DAY_COL)

def set_tweet_day(num, val):
	set_val(num, TWEET_DAY_COL, val)

def get_tweet_frequency(num):
	return get_val(num, TWEET_FREQUENCY_COL)

def set_tweet_frequency(num, val):
	set_val(num, TWEET_FREQUENCY_COL, val)

def get_tweet_time(num):
	return get_val(num, TWEET_TIME_COL)

def set_tweet_time(num, val):
	set_val(num, TWEET_TIME_COL, val)

def get_tweet_content(num):
	return get_val(num, TWEET_CONTENT_COL)

def set_tweet_content(num, val):
	set_val(num, TWEET_CONTENT_COL, val)


