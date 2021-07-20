import nltk
from text_processors.text_processor import TextProcessor


class StemmingProcessor(TextProcessor):

    def process(self, text):
        stemmer = nltk.porter.PorterStemmer()
        text = ' '.join([stemmer.stem(word) for word in text.split()])
        return TextProcessor.process(self, text)
