from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class VaderAnalyzer:

    def __init__(self, **vader_opts):
        self.vader_opts = vader_opts

    def __call__(self, data):
        analyzer = SentimentIntensityAnalyzer(**self.vader_opts)
        scores = analyzer.polarity_scores(data['text'])

        data['sentiment'] = {
            'score': scores['compound'],
            'extra': scores
        }

        return data
