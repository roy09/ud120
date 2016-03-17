#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


# Jeffrey Skilling
# print enron_data['SKILLING']

# missing POIs 3
# if a ml algo uses total_payment as a feature, would you expect it to associate with NaN value with POIs or non POIs?
print "Missing POIs 3:"
count = 0
for k in enron_data:
	if enron_data[k]['poi'] == True and enron_data[k]['total_payments'] == "NaN":
		count += 1
print count 

# missing POIs 4
print "Missing POIs 4:"
# number of people including new 10
print len(enron_data) + 10
# number of people with NaN for total payments
count = 0
for k in enron_data:
	if enron_data[k]['total_payments'] == "NaN":
		count += 1
print count + 10


# missing POIs 5
print "Missing POIs 5:"
# number of people who were POI
count = 0
for k in enron_data:
	if enron_data[k]['poi'] == True:
		count += 1
print count + 10

# percentage of people has NaN as total stock value
count = 0
for k in enron_data:
	if enron_data[k]['total_payments'] == "NaN" and enron_data[k]['poi'] == True:
		count += 1
count += 10
print count
print float(count) / (len(enron_data) + 10)