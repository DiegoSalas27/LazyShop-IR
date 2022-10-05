import abc
from pandas import DataFrame

# this is the interface for the file manager
class FileManager(metaclass=abc.ABCMeta): # formal way to define interfaces in python
  @classmethod
  def __subclasshook__(cls, subclass):
    return (hasattr(subclass, 'read_csv') and 
      callable(subclass.read_csv) and
      hasattr(subclass, 'access_group') and 
      callable(subclass.access_group))

  # abstract methods allows us to define functions for interfaces
  @abc.abstractmethod
  def read_csv(self, filename: str, encoding: str) -> DataFrame:
    """Read csv file using a given encoding and returns a dataframe"""
    raise NotImplementedError

  @abc.abstractmethod
  def access_group(self, filename: str, encoding: str) -> DataFrame:
    """Access a group of rows and columns by label(s) or a boolean array"""
    raise NotImplementedError