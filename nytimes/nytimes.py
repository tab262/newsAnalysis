
#!/usr/bin/python2.7 -S

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import time
import datetime
import csv
import json
import MySQLdb   #download
import feedparser#download
import imp

import getArticle
import getNYTHeadlines
import saveLoadHeadlines

#importing my own modules
articleAnalysis = imp.load_source('articleAnalysis', '/home/caseyso/Projects/newsAnalysis/newsAnalysis/analysis')

#####################################################

def main():
    nytimesRSS  = 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
    nytimesFeed = feedparser.parse(nytimesRSS)  #25 entries

    stories = getNYTHeadlines.get(nytimesFeed)
    print stories[1]
    
    saveLoadHeadlines.saveHeadlines(stories)
    
    

    
    
    
if __name__=="__main__": main()    
