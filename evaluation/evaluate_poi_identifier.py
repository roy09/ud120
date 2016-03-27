#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)


from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)


#1
prediction = clf.predict(features_test)
count = 0
for k in prediction:
	if k == 1:
		count += 1

print "Positive POI in result: ", count

#2
print "Total people in test set: ", len(prediction)

#3
print "Accuracy if all prediction is zero: ", (len(prediction) - float(count)) / len(prediction)

#4
for k in range(len(prediction)):
	print prediction[k], labels_test[k]

#5
from sklearn.metrics import precision_score, recall_score
print "Precision Score :", precision_score(prediction, labels_test)

#6
print "Recall Score :", recall_score(prediction, labels_test)

#7
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

count = 0
for k in range(len(predictions)):
	if predictions[k] == true_labels[k] and predictions[k] == 1:
		count += 1
print "TT: ", count

#8
count = 0
for i, j in zip(predictions, true_labels):
	if j == 0 and i == 0:
		count += 1
print "TF: ", count

#9
count = 0
for i, j in zip(predictions, true_labels):
	if i == 1 and j == 0:
		count += 1
print "FT: ", count

#10
count = 0
for i, j in zip(predictions, true_labels):
	if i == 0 and j == 1:
		count += 1
print "FN: ", count

#10
print "precision: ", precision_score(predictions, true_labels)

#11
print "recall: ", recall_score(predictions, true_labels)

