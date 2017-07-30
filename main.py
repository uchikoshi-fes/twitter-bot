#!/usr/bin/env python3

from setting import *
import spread_sheet as sheet
import slack

def make_notice_string(num):
	s = "[自動通知]\n"
	
	s += "※注意 現在テスト中です\n"
	
	s += "ツイート内容のリクエストがありました。\n"
	s += "リクエストのポスト時間 : "
	s += sheet.get_timestamp(num) + "\n"
	s += "リクエスト者 : " + sheet.get_mailaddr(num) + "\n"
	s += "ツイート回数 : "
	nt = sheet.get_tweet_num_times(num)
	s += nt
	s += "("
	if(nt == NUM_TIMES_ONCE):
		#s += NUM_TIMES_ONCE
		s += sheet.get_tweet_time(num)
	elif(nt == NUM_TIMES_REGULARLY):
		s += sheet.get_tweet_frequency(num)
	else:
		print(nt)
		s += "unkown num times value"
	s += ")\n"
	if(nt != NUM_TIMES_ONCE):
		s +=  "投稿時間: " 
		s += sheet.get_tweet_time(num) + "\n"
	s += "ツイート内容 : \n"
	s += "```\n"
	s += sheet.get_tweet_content(num) + "\n"
	s += "```\n"
	return s

# 許可申請メールを送る。ついでにSlackにも通知
def send_request(num):
	ns = make_notice_string(num)
	slack.post(ns)


# 溜まっているリクエストをチェックして、メールを送信
def check_request():
	i=0
	while 1:
		s = sheet.get_status(i)
		if(s == ""):
			break
		if(s == STATUS_PREPARE):
			send_request(i)
			sheet.set_status(i, STATUS_PERMISSION_WAIT)
		i+=1

# メールの返答をチェックして許可されていたらシートに反映
def check_mail():
	pass

# 許可されているツイートのうち、今ツイートするものをツイート
def tweet():
	pass


sheet.init()

check_request()

sheet.end()
