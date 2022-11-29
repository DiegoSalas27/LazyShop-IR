"""
AUTHOR: P Shiva Kumar / Diego Salas Noain
FILENAME: search_product_controller.py
SPECIFICATION: 
  - Need to have a point of entry for resolving a query and retrieving top 10 products
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
from services.search_similar_products_service import SearchSimilarProductsService

class SearchProductController:
  """
  NAME: __init__
  PARAMETERS: df, searchProduct, searchSimilarProducts, query
  PURPOSE: injects dependencies to this class
  PRECONDITION: The class is passed it's dependencies via instantiation
  POSTCONDITION: The class is injected searchProduct, searchSimilarProducts, df, query dependencies
  """
  def __init__(
    self, 
    df: DataFrame,
    searchProduct: SearchProductService,
    searchSimilarProducts: SearchSimilarProductsService,
    query: str):
      self.df = df
      self.searchProduct = searchProduct
      self.searchSimilarProducts = searchSimilarProducts
      self.query = query

  """
  NAME: execute
  PARAMETERS: none
  PURPOSE: Resolves a user query
  PRECONDITION: The zonal inverted index has been created and both the DataFrame and query are given
  POSTCONDITION: Retrieves top 10 documents based on tf_df ranking
  """
  def execute(self) -> list[int]:
    """Executes a series of services.
    \n\n returns what its implementation is meant to return"""
    posting_list = self.searchProduct.query_processing(self.query)
    term_freq, doc_freq = self.searchSimilarProducts.tf_df(posting_list)
    doc_score = self.searchSimilarProducts.doc_scoring(term_freq, doc_freq, self.df)
    top_10_docID = list(doc_score.keys())[0:10]
    
    return top_10_docID

    