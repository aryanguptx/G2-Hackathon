#Import all of joel's code
from Utilities.g2ApiResponse import getReviewResults
#Call function with parameter: Json output file path
review_list = getReviewResults("Utilities/g2ApiRespone.json")
#Response is a List of 2 Dictionaries
#print(type(review_list))
for dictionary in review_list:
    for key in dictionary:
        print(key, len(dictionary.get(key)))
#This response will call be sent as a parameter to the machinme learning model

