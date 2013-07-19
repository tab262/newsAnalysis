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
import time
import getArticle
import getNYTHeadlines
import saveLoadHeadlines
import getArticle
articleAnalysis = imp.load_source('articleAnalysis', '/home/gaddis/Projects/newsAnalysis/newsAnalysis/analysis')

def get(nytimesFeed):
    stories = {}
    print "Getting latest stories..."
    for i in range(len(nytimesFeed.entries)):
           
        date = nytimesFeed['entries'][i].published
        link = nytimesFeed['entries'][i].link 
        title = nytimesFeed.entries[i].title
        title = title.replace("'","")
        
        
        summary_detail = nytimesFeed.entries[i].summary_detail.value
        summary = summary_detail[:summary_detail.find('<img')]
        summary = list(summary)
        for j in range(len(summary)):
            if summary[j] == "'":
                summary[j] = ""
        summary = "".join(summary)

        ####Article analysis
        try:
            body =  getArticle.get(link + '&pagewanted=all')
            sents = body.split('.')
            words = body.split()
            AD = analysis(sents, words) #analysis dictionary
        except:
            try:
                body =  getArticle.get(link + '&pagewanted=all')
                sents = body.split('.')
                words = body.split()
                AD = analysis(sents, words) #analysis dictionary
            
            except:
                print(link)
        
        

        stories[i-1] = {'title' : title, 'summary' : summary, 'link' : link + '&pagewanted=all', 'date': date}
        try:
            for key in AD.keys():
                stories[i-1][key] = AD[key]
        except:
            print('getNYTHeadlines: Analysis lacking...')
        

    return stories
    
if __name__ == "__main__":
    nytimesRSS  = 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
    nytimesFeed = feedparser.parse(nytimesRSS)  #25 entries

    stories = getNYTHeadlines.get(nytimesFeed)
    
    
    





#############################################









###SCROLL DOWN TO MAIN TO FOLLOW ALONG###
###I recommend outputting to a text file (python articleAnalysis.py outputFile) to get a better idea of what it's doing

#creates a dict containing all trigrams and their counts
#Takes a list containing sentences 
def trigram(sentList):
    tgDict = {}
    for sent in sentList:
        words = sent.split()
        l = len(words)
        words.insert(0,'*')
        words.insert(0,'*')
        words.append('STOP')
        for i in range(l):
            tg = words[i],words[i+1],words[i+2]
            if tg not in tgDict:
                tgDict[tg] = 1
            elif tg in tgDict:
                tgDict[tg] += 1

    return tgDict

#creates a dict containing all bigrams and their counts
#takes a list containing sentences
def bigram(sentList):
    bgDict = {}
    for sent in sentList:
        words = sent.split()
        l = len(words)
        words.insert(0,'*')
        words.insert(0,'*')
        words.append('STOP')
        for i in range(l):
            bg = (words[i],words[i+1])
            if bg not in bgDict:
                bgDict[bg] = 1
            elif bg in bgDict:
                bgDict[bg] += 1
    return bgDict

#returns individual word counts
#takes a list of words 
def unigram(wordList):
    aDict = {}
    for word in wordList:
        if word[-2:] == "'s":
            string = word[:-2]
        else: 
            string = word
        
        if string in aDict:
            aDict[string] += 1
        else:
            aDict[string] = 1
    return aDict


#Can tinker with the setting here to look for common occuring grams of a given length and occurence
def gramAnalyzer(t,b,u):
    print('Unigrams')
    for key in u:
        if u[key] > 10 and len(key) > 3:
            print(key)
    print('Bigrams:')
    for key in b.keys():
        if b[key] > 1:
            print(key)
    
    print('Trigrams')
    for key in t.keys():
        if t[key] > 1:
            print(key)

#TODO: stop returns of words at the beginning of sentences
#Takes a list of individual words
#Solution to TODO would be to take a list of sents and toss the first word
def nounFinder(u):
    nounList = []
    for i in range(1,len(u)):
        prevchar = u[i-1][-1]
        nextChar = 'a'
        if i != len(u)-1:
            nextChar = u[i+1][0]
        
        if prevchar != '.' and u[i][0].isupper():
            if nextChar.isupper():
                string = u[i] + ' ' + u[i+1]
                nounList.append(string)
                i += 1
            else:
                nounList.append(u[i])
    return nounList

#cross checks nouns withs list of countries in external text file
def countryFinder(nouns):
    places = []
    countries = open('/home/caseyso/Projects/newsAnalysis/newsAnalysis/analysis/countries').read().split('\n')
    for word in nouns:
        if word in countries:
            places.append(word)
    return places
        

#Can tinker with settings here - should add arguments to the function so can pass parameters on the fly
def mostCommonWord(ugDict):
    max = 0
    word = ''
    for key in ugDict:
        if ugDict[key] > max and len(key) > 4 and key[0].isupper():
            max = ugDict[key]
            word = key
    return word


#Some stat functions for nlp
def trigramFreq(phrase,tgD,bgD):
    top = tgD[phrase]
    twoWords = phrase[:2]
    bottom = bgD[twoWords]
    return 1.0*top/bottom

def bigramFreq(phrase,bgD,ugD):
    if '*' not in phrase:
        top = bgD[phrase]
        oneWord = phrase[1]
        bottom = ugD[oneWord]
        return 1.0*top/bottom

def tupleToString(myTuple):
    l = len(myTuple)
    string = ''
    for i in range(l-1):
        string += myTuple[i]+' '
    string += myTuple[-1]
    return string

def freqCalculator(tgDict, bgDict,ugDict):
    for phrase in tgDict:
        prob = (trigramFreq(phrase, tgDict,bgDict))
        if prob != 1.0:
            print(tupleToString(phrase) + ' : ' +  str(prob))
    print('-'* 150)
    for phrase in bgDict:
        prob = bigramFreq(phrase,bgDict,ugDict)
        if prob != 1.0:
            print(tupleToString(phrase) + ' : ' + str(prob))


def getCommonGrams(tgDict, bgDict):
    commonTgs = []
    for key in tgDict.keys():
        if tgDict[key] > 2:
            commonTgs.append(key)
            
    commonBgs = []
    for key in bgDict.keys():
        if bgDict[key] > 3:
            commonBgs.append(key)
            
    return [commonTgs, commonBgs]

def prepForGrams(str_Article):
    sents = str_Article.split('.')
    
def getWordList(str_Article):
    return str_Article.split()
    

def analysis(sents, words):
    tgDict = trigram(sents)
    bgDict = bigram(sents)
    nouns = nounFinder(words)
    countries = countryFinder(nouns)
    commonGrams = getCommonGrams(tgDict, bgDict)
    analDict = {'nouns' : nouns, 'countries' : countries, 'commonGrams' : commonGrams }
    return analDict


