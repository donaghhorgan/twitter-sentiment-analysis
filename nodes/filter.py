class RetweetFilter:

    def __call__(self, data):
        tweet = data['status']
        if not tweet.retweeted and 'RT @' not in tweet.text:
            return data
