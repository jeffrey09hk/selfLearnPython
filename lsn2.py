# textblob - natural language processing
# this is for sentiment analysis

import tweepy
from textblob import TextBlob

consumer_key = 'nm9ODICwoYDDuRl28AvlUSNqD'
consumer_secret = '0y6bGHjNO4mERX53WlXh0luuKcpb6YWJNUSj2dtuC3ddCCO09W'

access_token = '308636052-UI8WysQSk4pIqq5W0ZBSskdO8DGYl7WmZTqryjLa'
access_secret = 's8Vi7RRQp5zWl1DtRjDTdIu6sXE5fDnolzNViZIh6U0Sp'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

public_tweets = api.search('spacejam11')

for tweet in public_tweets:
	print (tweet.text)
	analysis = TextBlob(tweet.text)
	print (analysis.sentiment)