from termcolor import cprint

from .twitter import get_tweet_text


class PrettyPrinter:

    def __init__(self, pos=1 / 3, neg=-1 / 3, show_scrubbed=False):
        self.pos = pos
        self.neg = neg
        self.show_scrubbed = show_scrubbed

    def get_colour(self, sentiment):
        if sentiment > self.pos:
            return 'green'
        elif sentiment < self.neg:
            return 'red'
        else:
            return 'grey'

    def __call__(self, data):
        colour = self.get_colour(data['sentiment']['score'])

        text = '-' * 80 + '\n\n'
        text += 'Original tweet: ' + get_tweet_text(data['status']) + '\n\n'
        text += 'Scrubbed tweet: ' + data['text'] + '\n\n' if self.show_scrubbed else ''
        text += 'Sentiment: {}'.format(data['sentiment']['score']) + '\n\n'
        text += '-' * 80

        cprint(text, colour)
