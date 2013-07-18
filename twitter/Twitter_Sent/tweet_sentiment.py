import sys
import urllib
import json

def getJsonFormat(sent_file, tweet_file):
    print 'Building sentiment dict...'
    scores = dictBuilder(sent_file)         #builds dictionary for sentiment scores
    print 'Loading json file...'
    results = json.load(tweet_file)          #uses json method to load file in list format
    
    return results

    sent_value = 0

def overallSentAnalysis(results):    
    'Scanning file for sentiment keywords...'
    for i in range(len(results)):
        if 'text' in results[i].keys(): #checks to see if item contains a tweet
            tweet = results[i]['text']
            tweetd = tweet.split()
            sent = ""
            sent_score = 0
            for word in tweetd:
                if word in scores:
                    sent = sent + word + "[" + str(scores[word]) + "] "
                    sent_score += scores[word]
                    sent_value += scores[word]
            if sent != "":
                pass
                #print sent, " TWEET SCORE:",  sent_score

    print "Total sentiment value:", sent_value
    
        
def lines(fp):
    print str(len(fp.readlines()))






def dictBuilder(filename):
    afinnfile = filename
    scores = {} #initializes empty dict
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def processData(fileName):
    print 'Reformatting data..'
    newContent = file(fileName, "r").read().replace("\r", "").replace("\n", ", ") #type: string
    #print type(newContent)
    newContent = newContent[:len(newContent)-2] #The last two chars become ", " I believe, gotta get rid of em
    print 'Writing to new file..'
    open(('p_'+fileName), "w").write(newContent)

#takes list object that contains dict
def indiviualTweetParser(tweet):
    pass

def getIndividualTweets(results):
    for tweet in results:
        try:
            print tweet['text'].encode('utf8')
        except:
            print 'No tweet'




def main():
    processData(sys.argv[2])                #formats data and saves the file as p_sys.argv[2]
    print 'Done processing file'
    sent_file = open(sys.argv[1])           #loads file containing sentiment data
    tweet_file = open(('p_' + sys.argv[2])) #loads formatted file
    results = getJsonFormat(sent_file, tweet_file)
    
    for key in results[67].keys():
        print '--' * 30
        print key + " : " + str(results[67][key].encode('utf8'))
        try:
            print '**' * 10
            print results[67][key].keys()
            print '--' * 3
        except:
            pass
    




if __name__ == '__main__':
    main()
