# textblob - natural language processing
# this is for sentiment analysis (understanding and extracting feelings from data)

import tweepy
import csv
import codecs
from textblob import TextBlob

# authenticate with tweepy to use its function
consumer_key = 'nm9ODICwoYDDuRl28AvlUSNqD'
consumer_secret = '0y6bGHjNO4mERX53WlXh0luuKcpb6YWJNUSj2dtuC3ddCCO09W'

access_token = '308636052-UI8WysQSk4pIqq5W0ZBSskdO8DGYl7WmZTqryjLa'
access_secret = 's8Vi7RRQp5zWl1DtRjDTdIu6sXE5fDnolzNViZIh6U0Sp'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Getting the tweets
public_tweets = api.search('illuminati')

for x in range(len(public_tweets)):
	tweetjson = public_tweets[x].text
	analysis = TextBlob(tweetjson)
	positivity = 'Positive'
	subjectivity = 'Objective'

	if analysis.polarity < 0:
		positivity = 'Negative'

	if analysis.subjectivity > 0.5:
		subjectivity = 'Subjective'

	entry = [tweetjson, analysis.polarity, analysis.subjectivity, positivity, subjectivity]
	# put tweet, polarity, subjectivity into csv
	with open('./lsn2.csv', 'a') as result:
		writer = csv.writer(result, dialect = 'excel')
		writer.writerows([entry])

result.close()

# subjectivity is the measure of how opinionated the text is
# polarity is the measure between -1 to 1, indicating the mood of the text