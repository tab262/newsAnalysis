import twitterstream
import tweet_sentiment




def main():
    afinnFile = open('AFINN-111.txt','r')
    while True:
        tweets = twitterstream.fetchsamples(200, afinnFile)
        
        


if __name__=="__main__": main()
