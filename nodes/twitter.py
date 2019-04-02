import logging
import queue

import tweepy


class TweetQueue(tweepy.StreamListener):

    def __init__(self):
        super(TweetQueue, self).__init__()
        self.queue = queue.Queue()

    def on_status(self, status):
        self.queue.put(status)

    def on_connect(self):
        logging.info('Stream connected')

    def on_disconnect(self, notice):
        logging.info('Stream disconnected: {}', notice)

    def on_warning(self, notice):
        logging.warning('Stream warning: {}', notice)

    def on_error(self, error_code):
        logging.error('Stream error: {}', error_code)

    def on_exception(self, exception):
        logging.exception('Stream exception: {}', exception)

    def on_timeout(self):
        logging.warning('Stream time out')

    def on_limit(self, track):
        logging.warning('Rate limit exceeded: {}', track)


class TwitterNode():

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, **filter_opts):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.filter_opts = filter_opts
        self.filter_opts['is_async'] = True  # Force asynchronous streaming

    def __call__(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)

        listener = TweetQueue()
        stream = tweepy.Stream(auth=auth, listener=listener)
        stream.filter(**self.filter_opts)

        while True:
            # Get the next status from the queue
            status = listener.queue.get()

            # Extract the tweet text
            if hasattr(status, 'extended_tweet'):
                text = status.extended_tweet['full_text']
            else:
                text = status.text

            yield {
                'status': status,
                'text': text,
                'time': status.created_at
            }
