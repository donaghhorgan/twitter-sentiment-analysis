import nltk
import textblob

nltk.download('movie_reviews')
nltk.download('punkt')

ANALYZERS = {
    'NaiveBayesAnalyzer': textblob.sentiments.NaiveBayesAnalyzer(),
    'PatternAnalyzer': textblob.sentiments.PatternAnalyzer()
}


class TextBlobAnalyzer:

    def __init__(self, **tb_opts):
        self.tb_opts = tb_opts

        # Translate analyzer names to classes
        analyzer = self.tb_opts.pop('analyzer', 'PatternAnalyzer')
        self.tb_opts['analyzer'] = ANALYZERS[analyzer]

    def __call__(self, data):
        tb = textblob.TextBlob(data['text'], **self.tb_opts)

        if hasattr(tb.sentiment, 'p_pos'):
            score = 2 * tb.sentiment.p_pos - 1
        else:
            score = tb.sentiment.polarity

        data['sentiment'] = {
            'score': score,
            'extra': tb.sentiment
        }

        return data
