import twitterstream
import tweet_sentiment
import json

def getTweets(numOfT, debug=False):

    print 'Getting tweets'
    tweets = twitterstream.fetchsamples(numOfT, debug)
    
    

    print 'Writing to file'
    writeFile = open('temp.json', 'w')

    writeFile.write('[')
    for i in range(numOfT):
        writeFile.write(tweets[i])
        if i < numOfT-1:
            writeFile.write(',\n')
    
    writeFile.write(']')

    writeFile.close()

    print 'Processing File'
    tweet_sentiment.processData('temp.json')

    print 'Obtaining results'
    readFile = open('temp.json','r')

    results = json.load(readFile)

    return results


def getField(tweets, fieldList):
    field = [] 
    if len(fieldList) == 1:
        for item in tweets:
            try:
                field.append(item[fieldList[0]].dencode('utf8'))
            except:
                print 'nope'
    if len(fieldList) == 2:
        for item in tweets:
            try:
                field.append(item[fieldList[0]][fieldList[1]].decode('utf8'))
            except:
                print 'nope'
    return field
 

def main():   
    r = getTweets(1000,True)
    locations = getField(r, ['user','location'])
    print locations


if __name__ == "__main__": main()
