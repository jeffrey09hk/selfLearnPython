# Link: https://www.youtube.com/watch?v=T5pRlIbr6gg
# module that let us make a decision tree
# from sklearn import tree 

# #[height, weight, shoe size]
# X = [[181, 80, 44], 
# 	[177, 70, 43],
# 	[160, 60, 38],
# 	[154, 54, 37],
# 	[166, 65, 40],
# 	[190, 90, 47], 
# 	[175, 64, 39], 
# 	[177, 70, 40],
# 	[159, 55, 37],
# 	[171, 75, 42], 
# 	[181, 85, 43]]

# Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 
# 	'female', 'male', 'male']

# # clf stands for classifier
# clf = tree.DecisionTreeClassifier()

# clf = clf.fit(X,Y)

# prediction = clf.predict([[190, 70, 43]])

# print (prediction)

# module that let us make a decision tree
from sklearn import svm

#[height, weight, shoe size]
X = [[181, 80, 44], 
	[177, 70, 43],
	[160, 60, 38],
	[154, 54, 37],
	[166, 65, 40],
	[190, 90, 47], 
	[175, 64, 39], 
	[177, 70, 40],
	[159, 55, 37],
	[171, 75, 42], 
	[181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 
	'female', 'male', 'male']

# clf stands for classifier
clf = svm.SVC()

clf = clf.fit(X,Y)

prediction = clf.predict([[190, 70, 31]])

print (prediction)