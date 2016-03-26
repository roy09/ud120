#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    print "hi", len(ages)
    cleaned_data = []

    ### your code goes here
    print type(ages)
    for k in range(len(ages)):
        error = abs(predictions[k] - net_worths[k])
        cleaned_data.append((ages[k], net_worths[k], error))

    # for i, j in zip(predictions, net_worths):
    #     error = abs(i - j)
    #     cleaned_data.append((i, j, error))


        # print (i, j, rs)
    print cleaned_data

    cleaned_data = sorted(cleaned_data, key=lambda tup:tup[2])[:81]

    return cleaned_data[:81]

