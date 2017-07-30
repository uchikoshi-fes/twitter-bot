from slacker import Slacker
from setting import *
import secret

def Slack():
	return Slacker(secret.SLACK_TOKEN)

def post(msg):
	s = Slack()
	s.chat.post_message(
		SLACK_CHANNEL,
		msg,
		username='tweet_request'
		)
