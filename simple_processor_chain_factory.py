from text_processors.html_tag import HtmlTagProcessor
from text_processors.accented_char import AccentedCharactersProcessor
from text_processors.special_char import SpecialCharProcessor
from text_processors.remove_number import RemoveNumberProcessor
from text_processors.punctuation_char import PunctuationCharactersProcessor
from text_processors.whitespace import WhitespaceCharactersProcessor
from text_processors.lower_case import LowerCaseProcessor


def create(next_processor=None):
    return HtmlTagProcessor(RemoveNumberProcessor(AccentedCharactersProcessor(
        SpecialCharProcessor(PunctuationCharactersProcessor(WhitespaceCharactersProcessor(
            LowerCaseProcessor(next_processor)))))))
