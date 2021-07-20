from text_processors.text_processor import TextProcessor
from bs4 import BeautifulSoup


class HtmlTagProcessor(TextProcessor):

    def process(self, text):
        text = BeautifulSoup(text, 'html.parser').get_text()
        return TextProcessor.process(self, text)
