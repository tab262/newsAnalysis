
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

def main():
    a = 'megaArticle'
    f  = open(a)
    sents = f.read().split('\n')
    f.close()
    words = open(a).read().split()
    tgDict = trigram(sents)
    bgDict = bigram(sents)
    ugDict = unigram(words)
    nouns = nounFinder(words)
    countries = countryFinder(nouns)
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
