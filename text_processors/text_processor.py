from abc import ABC


class TextProcessor(ABC):

    def __init__(self, next_processor=None):
        self.next = next_processor

    def process(self, text):
        if self.next:
            return self.next.process(text)
        else:
            return text
