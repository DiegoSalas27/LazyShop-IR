"""
AUTHOR: Diego Salas Noain
FILENAME: search_product_controller.py
SPECIFICATION: 
  - Need to have a point of entry for resolving a query
  - Create a controller class that can do that work
FOR: CS 5364 Information Retrieval Section 001 
"""

"""
NAME: SearchProductController 
PURPOSE: SearchProductController class is a class that executes the searchProduct service query processing function and retrieves all postings
INVARIANTS: There are no invariants
"""

from pandas import DataFrame
from services.search_product_service import SearchProductService

class SearchProductController:
  """
  NAME: __init__
  PARAMETERS: searchProduct, df, query
  PURPOSE: injects dependencies to this class
  PRECONDITION: The class is passed it's dependencies via instantiation
  POSTCONDITION: The class is injected searchProduct, df, query dependencies
  """
  def __init__(
    self, 
    searchProduct: SearchProductService,
    df: DataFrame,
    query: str):
      self.searchProduct = searchProduct
      self.df = df
      self.query = query

  """
  NAME: execute
  PARAMETERS: none
  PURPOSE: Resolves a user query
  PRECONDITION: The zonal inverted index has been created and both the DataFrame and query are given
  POSTCONDITION: Retrieves all postings and the documents
  """
  def execute(self) -> tuple[list[int], DataFrame]:
    """Executes a series of services.
    \n\n returns what its implementation is meant to return"""
    all_postings, act_docs = self.searchProduct.query_processing(self.query, self.df)
              
    return all_postings, act_docs

    