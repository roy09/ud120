#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
to = time()
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(features_train, labels_train)
print "training time: ", round(time()-to, 3), "s"

t1 = time()
print clf.score(features_test, labels_test)
print "prediction time: ", round(time()-t1, 3)
#########################################################

print len(features_test), len(labels_test)

from sklearn import svm

clf = svm.SVC(kernel="linear")
clf.fit(features_train, labels_train)

print "hi", clf.score(features_test, features_train)