from text_processors.text_processor import TextProcessor
import contractions


class ContractionProcessor(TextProcessor):

    def process(self, text):
        text = contractions.fix(text)
        return TextProcessor.process(self, text)
