import re
import unicodedata
from text_processors.text_processor import TextProcessor


class WhitespaceCharactersProcessor(TextProcessor):

    def process(self, text):
        pattern = r'^\s*|\s\s*'
        text = re.sub(pattern, ' ', text).strip()
        return TextProcessor.process(self, text)


