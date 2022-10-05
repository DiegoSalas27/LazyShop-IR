import abc
from typing_extensions import LiteralString

# this is the interface for the linguistic modules
class ModifyTokens(metaclass=abc.ABCMeta): # formal way to define interfaces in python
  @classmethod
  def __subclasshook__(cls, subclass):
    return (hasattr(subclass, 'stem') and 
      callable(subclass.stem) and 
      hasattr(subclass, 'string_replacement') and 
      callable(subclass.string_replacement) and 
      hasattr(subclass, 'modify_tokens') and 
      callable(subclass.modify_tokens))

  # abstract methods allows us to define functions for interfaces
  @abc.abstractmethod
  def stem(self, sentence_doc: list[str]) -> LiteralString: # private method
    """stems all words in doc and joins the stemmed tokens back into a sentence for further procesing
      \n\n returns the stemmed tokens as a sentence for further processing"""
    raise NotImplementedError

  @abc.abstractmethod
  def string_replacement(self, sentence_doc: list[str]) -> str: # private method
    """process the given string performing replacements using regex patterns 
      \n\n returns the replaced stemmed sentenced"""
    raise NotImplementedError

  @abc.abstractmethod
  def modify_tokens(self, sentence_doc: list[str]) -> list[str]:
    """process the given string performing replacements using business logic and deleting stop-words 
      \n\n returns the replaced senteced without stop-words"""
    raise NotImplementedError