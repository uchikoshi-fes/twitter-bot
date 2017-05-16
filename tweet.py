#!/usr/bin/env python3

from twitter import *
import twitter_keys as tk

def main():
	t = Twitter(auth=OAuth(tk.AT, tk.AS, tk.CK, tk.CS))

if __name__ == '__main__':
	main()
