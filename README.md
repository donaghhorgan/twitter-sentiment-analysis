# A sentiment analysis pipeline for Twitter

A [bonobo](https://www.bonobo-project.org/) pipeline for analysing sentiment from a live tweetstream. Supports lexical-based analysers ([pattern](https://www.clips.uantwerpen.be/pages/pattern-en) and [VADER](https://github.com/cjhutto/vaderSentiments)) and a Naive Bayes analyser ([textblob](https://textblob.readthedocs.io/en/dev/)). Prints tweet sentiment to the terminal.

This project was developed for [RebelCon 2019](https://rebelcon.io/). The accompanying presentation is available [here](https://donagh.io/talks/).

## Prerequisites

### Dependencies

Dependencies are managed with [pipenv](https://pipenv.readthedocs.io/en/latest/). Run `pipenv install` to create a virtual environment with the packages you need to run the pipeline.

### API credentials

Apply for [Developer API access](https://developer.twitter.com/), register a new app and make a note of your credentials. The pipeline will look for these in the environment variables `TWITTER_CONSUMER_KEY`, `TWITTER_CONSUMER_SECRET`, `TWITTER_ACCESS_TOKEN` and `TWITTER_ACCESS_TOKEN_SECRET`, so be sure to export these before running.

A handy way to avoid doing this every time is to define your credentials in a `.env` file, pipenv will automatically load them into the environment before running the pipeline.

## Usage

Export the API credentials or log them in a `.env` file as described above. Then run:

```bash
pipenv run ./app.py
```

This will load the default configuration (`config.yml`) and run it as a pipeline. You can specify alternate config files, if you like. Run `pipenv run ./app.py -h` for more info on how to do this.

### Filter tweets by topic or hashtag

The tweet stream can be filtered by topic by editing the `graph.tweetstream.config.track` property in your config file before running the pipeline. By default, `#brexit` is tracked but any query can be used, e.g. `boris johnson`.

### Use a different sentiment analyser

Currently, [pattern](https://www.clips.uantwerpen.be/pages/pattern-en), [textblob](https://textblob.readthedocs.io/en/dev/) and [VADER](https://github.com/cjhutto/vaderSentiments) analysers are supported. By default, VADER is used but this can be changed by modifying the `graph.sentiment_analyser.class` property to one of the following:

- pattern: `TextBlobPatternAnalyzer`
- textblob: `TextBlobNaiveBayesAnalyzer`
- VADER: `VaderAnalyzer`

### Change the terminal window colour thresholds

Edit `graph.pprint.config.pos` to change the threshold over which tweets are printed in green. Edit `graph.pprint.config.neg` to change the threshold below which tweets are printed in red.

### Do something else

The pipeline is written as a bonobo directed acyclic graph. You can add new functionality by adding a new node that instantiates whatever class or function you like.