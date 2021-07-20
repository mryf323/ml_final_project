from text_processors.text_processor import TextProcessor
import re


class SpecialCharProcessor(TextProcessor):

    def process(self, text):
        pat = r'[^a-zA-z0-9.,!?/:;\"\'\s]'
        text = re.sub(pat, ' ', text)
        return TextProcessor.process(self, text)
