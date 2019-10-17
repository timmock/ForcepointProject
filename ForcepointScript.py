import pandas as pd
import glob
import os
import json
import collections
import datetime
import re

inputpath = r'E:\Forcepoint Project\input' #where the input files are 
outputpath = r'E:\Forcepoint Project\output' #where the output files will be


allfiles = glob.glob(inputpath + "/*.csv")

content = []
prefix = []
truthyrows = []

#loop through all files
for filename in allfiles:
    #print(filename)
    #get the alpha prefix of the file
    prefixName = os.path.basename(filename).split('-')[0]
    prefix.append(prefixName)
    #print(prefixName)
    #check if the alpha prefix is virusScanResults
    if prefixName == "virusScanResults":
        with open(filename) as f:
            for row in f:
                firstVal = row.split(',')[0]
                #print(firstVal + "CXsdfsdf")
                #check if the first column is a truthy (since the values are being passed in as a string, we assume that these values do not pass the Truthy test)
                if firstVal not in ['false', 'False', 'none', 'None', '', ' ']:
                    #if it is, append the row for outputting
                    #print(bool(firstVal))
                    truthyrows.append(row) 

#filedict tells how many of each type of file there is (according to alpha refix)    
filedict = {i:prefix.count(i) for i in prefix}

data = {}
data['json'] = []
data['json'].append({
         "rules": [
            {
                'inputFileCounts' : filedict,
                'virusHits': truthyrows
            }
	]
})

isodate = re.sub('[^A-Za-z0-9]+', '', datetime.datetime.now().isoformat())
outputName = outputpath + "/" + "ABC" + isodate + ".json"

with open(outputName, 'w') as outfile:
    json.dump(data, outfile)

#def truthy_or_falsey(value):
#    print(value)
#    if value:
#        print(value + "true")
#        return True
#    else:
#        print(value + "fsfs")
#        return False

