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


def gramAnalyzer(t,b,u):
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

def countryFinder(nouns):
    places = []
    countries = open('countries').read().split('\n')
    for word in nouns:
        if word in countries:
            places.append(word)
    return places
        

def mostCommonWord(ugDict):
    max = 0
    word = ''
    for key in ugDict:
        if ugDict[key] > max and len(key) > 4 and key[0].isupper():
            max = ugDict[key]
            word = key
    return word

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


#star
def main():
    a = 'megaArticle'
    f  = open(a)
    
    #Makes a list of sentences. Right now it's more like mini-paragraphs as I break up by newlines and not periods
    #TODO: Get sentences and not paras
    sents = f.read().split('\n')
    f.close()
    
    #get list of individual words
    words = open(a).read().split()
    
    #trigrams are of sets three word sets ex: {(*,*,trigrams), (*,trigrams, are),(trigrams,are,sets),(are,sets,of)...etc}
    #creates a list of trigrams with their counts. High counts indicates words often appear together (i.e. President Obama)
    tgDict = trigram(sents)
    
    #same, but with two words
    bgDict = bigram(sents)
    
    #individual words and count
    ugDict = unigram(words)
    
    #this guy needs little work, but will return capitalized words. Still working out the kinks for it to avoid returning
    #words that are capitlized only because they occur at the begining of the sentence.
    nouns = nounFinder(words)
    
    #Checks to see if any of the nouns are countries
    #Could add a people finder, city finder, organization finder etc...
    countries = countryFinder(nouns)
    
    #Can uncomment these to see what sort of analysis is being returned
    #print(nouns)
    #gramAnalyzer(tgDict,bgDict,ugDict)
    mcw =(mostCommonWord(ugDict))
    for phrase in tgDict:
        prob = (trigramFreq(phrase, tgDict,bgDict))
        if prob != 1.0:
            print(tupleToString(phrase) + ' : ' +  str(prob))
    print('-'* 150)
    for phrase in bgDict:
        prob = bigramFreq(phrase,bgDict,ugDict)
        if prob != 1.0:
            print(tupleToString(phrase) + ' : ' + str(prob))

if __name__=="__main__": main()
