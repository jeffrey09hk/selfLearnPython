# Link: https://www.youtube.com/watch?v=9gBC9R-msAk

#Movie Recommender 

# There are two types of recommendation system
# 1. Collaborative System - Recommend what you like based on what other similar users have liked in the past 
# 2. Content-Based System - Recommend what you like based on what you have liked in the past

import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

# fetch data and format it
data = fetch_movielens(min_rating = 5.0)

# print training and testing data
 
print (repr(data['train']))
print (repr(data['test']))

# create model
# WARP = Weighted Approximate-Rank Pairwise
# Loss represents the loss function, measure the diff 
# between the models predictions and the desire output 


model = LightFM(loss = 'warp')
model.fit(data['train'], epochs = 30, num_threads = 2)

def sample_recommendation(model, data, user_ids):

	# number of users and movies in training data
	numUsers, numItems = data['train'].shape

	# generate recommednations for each user we input
	for user_id in user_ids:

		# movies the user already liked
		knownPositives = data['item_labels'][data['train'].tocsr()[user_id].indices]

		# movies our model predicts they will like
		scores = model.predict(user_id, np.arange(numItems))

		# rank them in order of most liked to least
		topItems = data['item_labels'][np.argsort(-scores)]

		# print out the results
		print ("User %s" % user_id)
		print ("	Known positives:")

		for x in knownPositives[:3]:
			print ("		%s" % x)

		print ("	Recommend: ")

		for x in topItems[:3]:
			print ("		%s" % x )

sample_recommendation(model, data, [500, 25, 450])