import pandas as pd
import glob
import os
import json
import collections
import datetime
import re

startTime = datetime.datetime.now()

inputpath = r'E:\Forcepoint Project\input' #where the input files are 
outputpath = r'E:\Forcepoint Project\output' #where the output files will be
outputalpha = "ABC"

allfiles = glob.glob(inputpath + "/*.csv")

prefix = []
truthyrows = []
lineAmt = 0

#loop through all files
for filename in allfiles:
    #get the alpha prefix of the file
    prefixName = os.path.basename(filename).split('-')[0]
    prefix.append(prefixName)
    #check if the alpha prefix is virusScanResults
    if prefixName == "virusScanResults":
        with open(filename) as f:
            for row in f:
                lineAmt = lineAmt + 1
                firstVal = row.split(',')[0]
                #check if the first column is a truthy (since the values are being passed in as a string, we assume that these values do not pass the Truthy test)
                if firstVal not in ['false', 'False', 'none', 'None', '', ' ']:
                    #if it is, append the row for outputting
                    truthyrows.append(row) 

#filedict tells how many of each type of file there is (according to alpha refix)    
filedict = {i:prefix.count(i) for i in prefix}

#processing time is how long it took
endTime = datetime.datetime.now()
processtime = endTime - startTime

data = {}
data['json'] = []
data['json'].append({
     "metadata" : {
         "start time" : str(startTime),
         "end time" : str(endTime),
         "process time": str(processtime) + ' seconds',
         "total number of virus hits" : len(truthyrows),
         "total number of files read" : len(allfiles),
         "total number of virus lines scanned" : lineAmt
     },
     "data" : {
         "rules": [
            {
                'inputFileCounts' : filedict,
                'virusHits': truthyrows
            }
         ]
     }
})

isodate = re.sub('[^A-Za-z0-9]+', '', datetime.datetime.now().isoformat())
outputName = outputpath + "/" + outputalpha + isodate + ".json"

with open(outputName, 'w') as outfile:
    json.dump(data, outfile)
