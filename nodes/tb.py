import abc
import nltk
import textblob

nltk.download('movie_reviews')
nltk.download('punkt')


class TextBlobAnalyzer(abc.ABC):

    def __init__(self, analyzer, **tb_opts):
        self.tb_opts = tb_opts
        self.tb_opts['analyzer'] = analyzer

    @staticmethod
    @abc.abstractmethod
    def get_sentiment_score(tb):
        pass

    def __call__(self, data):
        tb = textblob.TextBlob(data['text'], **self.tb_opts)

        data['sentiment'] = {
            'score': self.get_sentiment_score(tb),
            'extra': tb.sentiment
        }

        return data


class TextBlobNaiveBayesAnalyzer(TextBlobAnalyzer):

    def __init__(self, **tb_opts):
        super(TextBlobNaiveBayesAnalyzer, self).__init__(textblob.sentiments.NaiveBayesAnalyzer(), **tb_opts)

    @staticmethod
    def get_sentiment_score(tb):
        return 2 * tb.sentiment.p_pos - 1


class TextBlobPatternAnalyzer(TextBlobAnalyzer):

    def __init__(self, **tb_opts):
        super(TextBlobPatternAnalyzer, self).__init__(textblob.sentiments.PatternAnalyzer(), **tb_opts)

    @staticmethod
    def get_sentiment_score(tb):
        return tb.sentiment.polarity
