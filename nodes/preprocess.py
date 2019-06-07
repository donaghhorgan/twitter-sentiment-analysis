import re


def remove_pattern(pattern, tweet):
    return re.sub(pattern, '', tweet)


def trim_retweet_handles(tweet):
    return remove_pattern('RT @\w+:', tweet)


def trim_usernames(tweet):
    return remove_pattern('@\w+', tweet)


def trim_urls(tweet):
    return remove_pattern('https?://[\w./]*', tweet)


def split_hashtags(tweet):
    hashtags = re.findall('\#\w+', tweet)
    for hashtag in hashtags:
        tweet = re.sub(hashtag, re.sub('([A-Z])+', r' \1', hashtag[1:]), tweet)
    return tweet


class TweetCleaner:

    def __init__(self, remove_retweet_handles=False, remove_usernames=False, remove_urls=False, split_hashtags=False):
        self.remove_retweet_handles = remove_retweet_handles
        self.remove_usernames = remove_usernames
        self.remove_urls = remove_urls
        self.split_hashtags = split_hashtags

    def __call__(self, data):
        if self.remove_retweet_handles:
            data['text'] = trim_retweet_handles(data['text'])

        if self.remove_usernames:
            data['text'] = trim_usernames(data['text'])

        if self.remove_urls:
            data['text'] = trim_urls(data['text'])

        if self.split_hashtags:
            data['text'] = split_hashtags(data['text'])

        return data
