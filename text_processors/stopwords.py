import nltk
from text_processors.text_processor import TextProcessor
from nltk.tokenize import ToktokTokenizer


class StopwordProcessor(TextProcessor):
    tokenizer = ToktokTokenizer()
    stopword_list = nltk.corpus.stopwords.words('english')
    stopword_list.remove('not')

    def process(self, text):
        tokens = StopwordProcessor.tokenizer.tokenize(text)
        tokens = [token.strip() for token in tokens]
        t = [token for token in tokens if token.lower() not in StopwordProcessor.stopword_list]
        text = ' '.join(t)
        return TextProcessor.process(self, text)
