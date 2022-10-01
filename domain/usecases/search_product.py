import abc
from domain.models.query_result import QueryResult

# this is the interface for the indexer
class SearchProduct(metaclass=abc.ABCMeta): # formal way to define interfaces in python
  @classmethod
  def __subclasshook__(cls, subclass):
    return (hasattr(subclass, 'tokenize') and 
      callable(subclass.tokenize))

  # abstract methods allows us to define functions for interfaces
  @abc.abstractmethod
  def query_processing(self, query: str) ->  QueryResult:
    """Search for a product based given a query string using an inverted index
      \n\n returns a QueryResult"""
    raise NotImplementedError