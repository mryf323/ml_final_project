import nltk
import numpy as np
from nltk.tokenize import word_tokenize
from text_processors.text_processor import TextProcessor


class StemmingProcessor(TextProcessor):
    stemmer = nltk.porter.PorterStemmer()

    def process(self, text):
        text = ' '.join([StemmingProcessor.stemmer.stem(word) for word in text.split()])
        return TextProcessor.process(self, text)
