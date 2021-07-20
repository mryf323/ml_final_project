import simple_processor_chain_factory
from text_processors.contraction import ContractionProcessor
from text_processors.lemmatization import LemmatizationProcessor
from text_processors.stemming import StemmingProcessor
from text_processors.stopwords import StopwordProcessor


def create(word_root_strategy='lem'):
    if word_root_strategy is 'lem':
        chain = LemmatizationProcessor()
    else:
        chain = StemmingProcessor()
    return ContractionProcessor(simple_processor_chain_factory.create(StopwordProcessor(chain)))

