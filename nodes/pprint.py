from termcolor import cprint


def get_colour(sentiment):
    if sentiment > 1 / 3:
        return 'green'
    elif sentiment < -1 / 3:
        return 'red'
    else:
        return 'grey'


class PrettyPrinterNode:

    def __call__(self, data):
        colour = get_colour(data['sentiment'])

        text = '-' * 80 + '\n\n'
        text += data['text'] + '\n\n'
        text += 'Sentiment: {}'.format(data['sentiment']) + '\n\n'
        text += '-' * 80

        cprint(text, colour)
