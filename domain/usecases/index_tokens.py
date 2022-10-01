import abc
from pandas import DataFrame

# this is the interface for the indexer
class IndexTokens(metaclass=abc.ABCMeta): # formal way to define interfaces in python
  @classmethod
  def __subclasshook__(cls, subclass):
    return (hasattr(subclass, 'tokenize') and 
      callable(subclass.tokenize))

  # abstract methods allows us to define functions for interfaces
  @abc.abstractmethod
  def build_inverted_index(self, zone: str, docID: int, modified_tokens: list[str]) -> dict[str, dict]:
    """Builds the inverted index based on the modified tokens from the linguistic modules
      \n\n returns the inverted index dictionary"""
    raise NotImplementedError