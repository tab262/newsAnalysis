import twitterSearch
import getGeoCoords

def processTweets(tweets):
    for i in range(len(tweets['statuses'])):
        text = (tweets['statuses'][i]['text'])
        user = (tweets['statuses'][i]['user']['screen_name'])
        time = (tweets['statuses'][i]['created_at'])
        print(user + '(' + time + "): " + text + '\n')


print("Welcome! This program allows you type in an address and look at tweets within a specified radius of that location.\nType in the address if you were searching google maps (i.e. 1234 Soldiers Field Road, Boston, MA).\nThe program will also ask you to specify a radius in miles.\n\n\n")
while True:
    address = str(raw_input("Enter the address(q to quit): "))
    if address.lower() == 'q':
        break
    
    distance = str(raw_input("Distance from address to search: ")) + 'mi'
    geoCoords = getGeoCoords.getGeoCoords(address)
    print("The GPS coordinates are([lat, lng]): " + str(geoCoords))
    print('Let\'s get some tweets...\nThis might take a moment...\n\n')
    arg = 'geocode:' + str(geoCoords[0]) + ',' + str(geoCoords[1]) + ',' + distance
    tweets = twitterSearch.search(arg)
    p_tweets = processTweets(tweets)


    

    
    
