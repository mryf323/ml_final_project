import unicodedata
from text_processors.text_processor import TextProcessor


class AccentedCharactersProcessor(TextProcessor):

    def process(self, text):
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        return TextProcessor.process(self, text)


