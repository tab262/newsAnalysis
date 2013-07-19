import twitterSearch

def get(user):
	url = "from%3A "+ user + "&src=typd"
	userTweets = twitterSearch.searchUser(url)
	return userTweets
	
def main():
	tweets = get('mattyjay14')
	print type(tweets['statuses'])
	print len(tweets['statuses'])
	print(tweets['statuses'][0].keys())
	print(tweets['statuses'][1]['created_at'])

if __name__=="__main__": main()
