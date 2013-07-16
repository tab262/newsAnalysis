import mechanize
from BeautifulSoup import BeautifulSoup
import re

def getHtmlText(url):

    br = mechanize.Browser()
    #br.set_handle_robots(False)

    HT = br.open(url).read()
    return HT



def getMainTextBody(htmlText):
    HT = htmlText
    l = len('<p itemprop="articleBody">')
    text = [] 
    while True:
        stIndex = 0
        enIndex = 0
        stIndex = HT.find('<p itemprop="articleBody">')
        enIndex = HT[stIndex:].find('</p>') + stIndex
        if stIndex == -1 or enIndex == -1:
            break
        string = (HT[stIndex+l:enIndex]).decode('utf8').split()
        for word in string:
            text.append(word)
        HT = HT[enIndex:]

    
    textString = ''
    for item in text:
        textString = textString + item + ' '
    return textString


##MAIN FUNCTION
def get(url):
    HT = getHtmlText(url)
    body = getMainTextBody(HT)
    return body    
    
    
