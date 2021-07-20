import spacy
from text_processors.text_processor import TextProcessor


class LemmatizationProcessor(TextProcessor):
    nlp = spacy.load('en_core_web_sm')

    def process(self, text):
        doc = LemmatizationProcessor.nlp(text)
        text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in doc])
        return TextProcessor.process(self, text)
