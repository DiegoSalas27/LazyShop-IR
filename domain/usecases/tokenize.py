import abc
from typing import Any

# this is the interface for the tokenizer
class Tokenize(metaclass=abc.ABCMeta): # formal way to define interfaces in python
  @classmethod
  def __subclasshook__(cls, subclass):
    return (hasattr(subclass, 'tokenize') and 
      callable(subclass.tokenize))

  # abstract methods allows us to define functions for interfaces
  @abc.abstractmethod
  def tokenize(self, doc: Any) -> list[str]:
    """Tokenises the words in the row of the selected zone
      \n\n returns all the lists of the rows of each selected zone"""
    raise NotImplementedError