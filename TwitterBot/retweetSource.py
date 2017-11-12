#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Import Tweepy, sleep, credentials.py
import tweepy 
from time import sleep


# Access and authorize our Twitter credentials from credentials.py
def main():
	consumer_key = 'ezT5j0pRtCakw3O1pN8PjeQF7'
	consumer_secret = 'wVflXWNj7pC3lGwhMelaEX4AYZReUHazXlZ8R6veAGY2oeFjkt'
	access_key = '889485691675127809-63aEoWJytHS4TYVR6KA1MWz15yI6WV7'
	access_key_secret = 'rdKzsxKuYkRimPA8IFyQApll5wN0m0sXZB6f50L0XIi8x'

	grape = tweepy.api(consumer_key = consumer_key,
					 consumer_secret = consumer_secret,
					 access_token_key = access_key,
					 access_token_secret = access_key_secret)
	grape.update_status("tweet test")
	print("tweet sent")



main()
