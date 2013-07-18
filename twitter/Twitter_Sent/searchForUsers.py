import twitterstream
import tweet_sentiment
import getTweets
import json

#assume we have a set of tweets to be passed into our search
#returns set of tweets with users from a given location
def getUsersFromLocation(tweets, location):
    tweetsOfInterest = []
    usersOfInterest = []
    for item in tweets:
        if (item['user']['location']).lowercase() == location.lowercase():
            tweetsOfInterest.append(item)
            usersOfInterest.append(item['user'])

def getPercentUsersWithLocation(tweets):
    withLoc = 0
    woLoc   = 0
    bostonUsers = []
    for item in tweets:
        loc = ''
        try:
            loc = item['user']['location']
            print(loc)
            if len(loc) > 0:
                withLoc = withLoc + 1
                if loc.lower() == 'boston' or 'boston' in loc.lower().split() or 'boston,' in loc.lower().split():
                    bostonUsers.append(item['user']['screen_name'])
            else:
                woLoc = woLoc + 1
        except:
            print('Location field missing')

       
    print('with',withLoc)
    print('wo',woLoc)

    return [(1.0 * withLoc/(withLoc + woLoc)), bostonUsers]

def main():
    results = getTweets.getTweets(10000,True)
 
    bostonUsers = (getPercentUsersWithLocation(results))[1]
    f = open('bostonUsers','a')
    for i in range(len(bostonUsers)):
        f.write(bostonUsers[i])
        f.write('\n')
    print(bostonUsers)


if __name__ == "__main__": main()
