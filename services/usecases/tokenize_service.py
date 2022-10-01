from typing import Any
from domain.usecases.tokenize import Tokenize
from services.protocols.nl_util import NlUtil

# this class implements the tokenize interface
class TokenizeService(Tokenize):
  def __init__(self, nlUtil: NlUtil):
    self.nlUtil = nlUtil
  
  def tokenize(self, doc: Any) -> list[str]:
    sentence_doc = self.nlUtil.word_tokenizer(str(doc)) # list[str,];

    return sentence_doc