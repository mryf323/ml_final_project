from text_processors.text_processor import TextProcessor


class LowerCaseProcessor(TextProcessor):

    def process(self, text):
        text = text.lower()
        return TextProcessor.process(self, text)

