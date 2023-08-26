"""
AUTHOR: P Shiva Kumar / Diego Salas Noain
FILENAME: tokenizer.py
SPECIFICATION: 
  - We need to tokenize the data
  - We create a utility class that can perform tokenization
  - We should retrieve tokens ready to by used by linguistic modules
FOR: CS 5364 Information Retrieval Section 001 
"""

"""
NAME: Tokenizer 
PURPOSE: Tokenizer class is a utility class that tokenies each document given
INVARIANTS: There are no invariants
"""

from nltk.tokenize import word_tokenize
from typing import Any

# this class implements the tokenizer
class Tokenizer:
  """
  NAME: tokenize
  PARAMETERS: doc
  PURPOSE: Tokenises the words in the row of the selected zone
  PRECONDITION: a document is given
  POSTCONDITION: returns all the lists of the rows of each selected zone
  """
  @staticmethod
  def tokenize(doc: Any) -> list[str]:
    """Tokenises the words in the row of the selected zone
    \n\n returns all the lists of the rows of each selected zone"""
    return word_tokenize(str(doc)) # list[str,];