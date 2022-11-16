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
import numpy as np
from pandas import DataFrame
from services.search_product_service import SearchProductService
from services.search_similar_products_service import SearchSimilarProductsService

class SearchSimilarProductsController:
  """
  NAME: __init__
  PARAMETERS: searchProduct, df, query
  PURPOSE: injects dependencies to this class
  PRECONDITION: The class is passed it's dependencies via instantiation
  POSTCONDITION: The class is injected searchProduct, df, query dependencies
  """
  def __init__(
    self, 
    df: DataFrame,
    searchProduct: SearchProductService,
    searchSimilarProducts: SearchSimilarProductsService,
    name: str):
      self.df = df
      self.searchSimilarProducts = searchSimilarProducts
      self.searchProduct = searchProduct
      self.name = name

  """
  NAME: execute
  PARAMETERS: none
  PURPOSE: Resolves a user query
  PRECONDITION: The zonal inverted index has been created and both the DataFrame and query are given
  POSTCONDITION: Retrieves all postings and the documents
  """
  def execute(self) -> dict[int, float]:
    """Executes a series of services.
    \n\n returns what its implementation is meant to return"""
    initiate_query_bow, initiate_bow = self.searchSimilarProducts.preprocess(self.df)
    bow, L2_norm_doc = self.searchSimilarProducts.BOW(self.df, initiate_bow)
    query_bow, L2_norm_query = self.searchSimilarProducts.query_BOW(self.name, initiate_query_bow, bow)
    L2_reciprocal = np.multiply(L2_norm_query,L2_norm_doc)
    L2_product = 1/L2_reciprocal
    query_matrix = query_bow.to_numpy()
    doc_matrix = bow.to_numpy()
    dot_pdt = np.dot(doc_matrix, query_matrix.T)
    dot_pdt = dot_pdt.flatten()
    dot_pdt
    cos_similarity = np.multiply(dot_pdt, L2_product)
    cos_similarity = cos_similarity.tolist()
    cos_similarity = enumerate(cos_similarity)
    cos_similarity = dict(cos_similarity)
    cos_similarity = dict(sorted(cos_similarity.items(), key = lambda x : x[1], reverse= True))
    cos_similarity
              
    return cos_similarity

    