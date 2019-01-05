import tweepy
from textblob import TextBlob

consumer_key = 'BoH28mT8PTlEk8gUKgQMe8M10'
consumer_secret = '5KfzZj6t3yLxoMMvcnIugqTEV2FgBRBm0ySxNdZjiaxRn6BnBZ'

access_token = '1337023771-UDhFNhLbL65EXDGTp0ogF8KlP3rliQXk1AsItaL'
access_token_secret = 'Bh0o88XYJeib5KSsmrUDvrH8cmXRwu7czWSkTTKtpsPyq'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Duterte')

for tweet in public_tweets:
       print(tweet.text)
       analysis = TextBlob(tweet.text)
       print(analysis.sentiment)