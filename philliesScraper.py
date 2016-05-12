# Python's batteries-included url library
from urllib.request import urlopen
from urllib.error import HTTPError

# Python module for JSON enconding/decoding
import json

# Beautiful Soup 4 library
from bs4 import BeautifulSoup

# For observing program runtime
# import math
from datetime import datetime, timedelta

def getPage(url):
    # varibale for recording script runtime
    start = datetime.now()
    try:
        html = urlopen(url)
        print(type(html))
    except HTTPError as e:
        print("Encountered an error: " + e)
        return e
    try:
        soupd = BeautifulSoup(html.read(), "html.parser")
        timeTaken = datetime.now() - start
        print("Duration of function call (url accessing + BS creation): " +
            str(round(((timeTaken.days * 86400 + timeTaken.seconds) / 60), 4)) +
            " seconds")
    except AttributeError as e:
        print("Error creating the BS object")
        timeTaken = datetime.now() - start
        print("Duration of function call (url accessing + BS creation): " +
            str(round( ((timeTaken.days * 86400 + timeTaken.seconds)/60), 4) ) +
            " seconds")
        return none
    return soupd

bsObject = getPage("http://www.baseball-reference.com/teams/PHI/2016.shtml")
print("The type of " + str(type(bsObject.title)))

#



with open('output/sports.json', 'w') as outputFile:
    json.dumps()
