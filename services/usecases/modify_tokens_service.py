import re
from string import punctuation
from typing_extensions import LiteralString
from domain.usecases.modify_tokens import ModifyTokens
from services.protocols.nl_util import NlUtil

# this class implements the linguistic modules interface
class ModifyTokensService(ModifyTokens):
  def __init__(self, nlUtil: NlUtil):
    self.nlUtil = nlUtil

  def _stem(self, sentence_doc: list[str]) -> LiteralString: # private method
    # stems all words in doc
    sentence_str_1 = [self.nlUtil.word_stemmer(word_tk) for word_tk in sentence_doc]  # list[str,]
    # joins the stemmed tokens back into a sentence for further procesing
    sentence_str_1 = " ".join(sentence_str_1) # str

    return sentence_str_1

  def _string_replacement(self, sentence_doc: list[str]) -> str: # private method
    stemmed_sentence = self._stem(sentence_doc)
    # subs all symbols/punctuations (including space) with a space (' '); excludes digits
    replaced_str = re.sub(r'\W+', ' ', stemmed_sentence)
    # subs all digits with a space (' '); a sequence of digits (without space) is given one (' ')
    replaced_str = re.sub(r'\d+', ' ', replaced_str)
    # subs all symbols AND digits (including spaces) with a space (' '); includes digits
    replaced_str = re.sub(r'[^a-zA-Z]', ' ', replaced_str)
    # compiles a pattern and subs out the pattern in stemmed_sentence with ' '
    replaced_str = re.compile('(\s*)pron(\s*)').sub(' ', replaced_str)

    return replaced_str

  def modify_tokens(self, sentence_doc: list[str]) -> list[str]:
    replaced_string = self._string_replacement(sentence_doc)

    # tokenize to clean up one more time if 're' has introduced and garbage
    modified_tokens = self.nlUtil.word_tokenizer(replaced_string) # list[str,]
    # strip removes whitespace at beginning and end of string (not in between)
    modified_tokens = [str(word_tk_1).strip() for word_tk_1 in modified_tokens] # list[str,]
    # strings with >=2 chars only
    modified_tokens  = [word_str for word_str in modified_tokens if len(word_str) >= 2] # list[str,]
    # strings which are not symbols/punctuations
    modified_tokens = [word_str for word_str in modified_tokens  if word_str not in punctuation]
    # strings which are not stop-words; check with: Spacy_Eng.vocab['word'].is_stop
    modified_tokens = [word_str for word_str in modified_tokens if word_str not in self.nlUtil.stop_words()]

    return modified_tokens