
#!/usr/bin/python2.7 -S

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import time
import datetime
import csv
import json
#import MySQLdb   #download
import feedparser#download
import imp

import getArticle
import getNYTHeadlines
import saveLoadHeadlines

#importing my own modules
articleAnalysis = imp.load_source('articleAnalysis', '/home/gaddis/Projects/newsAnalysis/newsAnalysis/analysis')

#####################################################

def main():
    nytimesRSS  = 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
    nytimesFeed = feedparser.parse(nytimesRSS)  #25 entries

    stories = getNYTHeadlines.get(nytimesFeed)
    
    #weird quirk - bug somewhere in getNYTHeadlines has to do some 
    #indexing kung fu. This bit here fixes it. I know...bad programmer, bad!
    temp = stories[0]
    stories[0] = stories[-1]
    stories[-1] = temp
    
    saveLoadHeadlines.saveHeadlines(stories)
    
    

    
    
    
if __name__=="__main__": main()    
