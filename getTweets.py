import tweepy
from tweepy import OAuthHandler
import json
 
consumer_key = '1UMSrg9dPB1jDYZquR7hWD5oJ'
consumer_secret = 'zUVZtyVi1QUzNbtNaZ7h8MxrCbcezMCz678NCa4Cii8dB5kNUX'
access_token = '3171483675-tm2KompTxm6GWKZUuLe9VGHhKV41QLC8eK6tYzh'
access_secret = 'lYX56p7bIah2Y2ssxAUCtm4vV36mTH50LMWfgzuXNDtwg'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

def process_or_store(tweet):
    try:
    	place = tweet['place']['full_name']
    	if place != 'Berkeley, CA':
    		raise AssertionError
    	else:
    		print(tweet['text'])
    		print(place)
    except:
    	pass
    
for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)