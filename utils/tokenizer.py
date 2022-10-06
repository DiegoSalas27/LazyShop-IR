from nltk.tokenize import word_tokenize
from typing import Any

# this class implements the tokenizer
class Tokenizer:

  @staticmethod
  def tokenize(doc: Any) -> list[str]:
    """Tokenises the words in the row of the selected zone
    \n\n returns all the lists of the rows of each selected zone"""
    return word_tokenize(str(doc)) # list[str,];