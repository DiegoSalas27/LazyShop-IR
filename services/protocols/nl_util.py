import abc

# this is the interface for the Natural Langue Util
class NlUtil(metaclass=abc.ABCMeta): # formal way to define interfaces in python
  @classmethod
  def __subclasshook__(cls, subclass):
    return (hasattr(subclass, 'word_tokenizer') and 
      callable(subclass.word_tokenizer) and
      hasattr(subclass, 'word_stemmer') and 
      callable(subclass.word_stemmer) and
      hasattr(subclass, 'stop_words') and 
      callable(subclass.stop_words))

  # abstract methods allows us to define functions for interfaces
  @abc.abstractmethod
  def word_tokenizer(self, rowString: str) -> list[str]:
    """Tokenises the words in the row of the selected zone based on NLTK vocab"""
    raise NotImplementedError

  @abc.abstractmethod
  def word_stemmer(self, word: str) -> str:
    """Stems a word"""
    raise NotImplementedError

  @abc.abstractmethod
  def stop_words(self) -> set:
    """returns a list of stop words"""
    raise NotImplementedError