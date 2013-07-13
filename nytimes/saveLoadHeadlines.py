import datetime
import csv
import json

def saveHeadlines(headlineDict):
    now = datetime.datetime.now()
    filename = "headlines-"+str(now.year)+'-'+str(now.month)+'-'+ \
        str(now.day)+'-'+str(now.hour)+'_'+str(now.minute)+'.json'
    json.dump(headlineDict, open(filename, 'wb'))
    
    print filename
    newDict = json.load(open(filename))
    #print newDict['0']['title'] 
    
def loadHeadLines(headlinesFile):
    return json.load(open(headlinesFile))

