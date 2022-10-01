import abc
from typing import Any

# this is the interface for the controllers
class Controller(metaclass=abc.ABCMeta): # formal way to define interfaces in python
  @classmethod
  def __subclasshook__(cls, subclass):
    return (hasattr(subclass, 'execute') and 
      callable(subclass.execute))

  # abstract methods allows us to define functions for interfaces
  @abc.abstractmethod
  def execute(self) -> Any:
    """Executes a series of services.
      \n\n returns what its implementation is meant to return"""
    raise NotImplementedError