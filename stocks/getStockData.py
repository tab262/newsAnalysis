import urllib
import re
import json
import time
#epoch time 1371573000000 #has three too many zerps
#convert: time.gmtime(1371573000000)

def epochToGmt(epochT):
    epoStr = str(epochT)
    epoStr = epoStr[:10]
    epoInt = int(epoStr)
    return time.gmtime(epoInt)

def epochStructFormat(eStruct, p=None):
    timeUnit = ['year', 'month','day','hour','minute', 'sec','wday','yday','isdst']
    timeDict = {}
    for i in range(len(eStruct)):
        timeDict[timeUnit[i]] = str(eStruct[i])
        if p == 'p':
            print timeUnit[i] + ': ' + str(eStruct[i])
    return timeDict


def getStockDayData(stock):
    stock = stock.upper()
    htmltext = urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/" + stock +":US").read()
    data = json.loads(htmltext)
    return data

def getTimePrices(data):
    prices = data['data_values']
    print(len(prices))
    
    for i in range(len(prices)):
        time = epochToGmt(prices[i][0])
        time = epochStructFormat(time)
        if int(time['minute']) < 10:
            time['minute'] = '0' + time['minute']
        prices[i][0] = time['hour'] + ':' + time['minute']

    return prices

def get(stock):
    data = getStockDayData(stock)
    

    return data

if __name__=="__main__":
    stock = str(raw_input("Stock Symbol: "))
    data = get(stock)
    prices = getTimePrices(data)
    print(prices)
