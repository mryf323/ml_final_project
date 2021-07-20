from text_processors.text_processor import TextProcessor
import re


class RemoveNumberProcessor(TextProcessor):

    def process(self, text):
        pattern = r'[0-9]+'
        text = re.sub(pattern, ' ', text)
        return TextProcessor.process(self, text)
