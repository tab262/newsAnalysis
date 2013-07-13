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
import getArticle

nytimesRSS  = 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'

nytimesFeed = feedparser.parse(nytimesRSS)  #25 entries


def main():
    
    stories = getNYTHeadLines()
    link1 = stories[1]['link']+'&pagewanted=all'
    print(link1)
    body = getArticle.get(link1)
    print len(body)
    
    
    
    

    
    
    
if __name__=="__main__": main()    
