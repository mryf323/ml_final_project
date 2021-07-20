from text_processors.text_processor import TextProcessor
import string


class PunctuationCharactersProcessor(TextProcessor):

    def process(self, text):
        text = ''.join([c for c in text if c not in string.punctuation])
        return TextProcessor.process(self, text)
