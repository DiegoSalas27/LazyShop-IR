"""
AUTHOR: Diego Salas Noain
FILENAME: search_similar_products_controller.py
SPECIFICATION:  
  - Need to have a point of entry for solving a query based on a product name
  - Based on a query retrieve the all similar documents in order 
  - Create a controller class to do it
FOR: CS 5364 Information Retrieval Section 001 
"""

"""
NAME: SearchSimilarProductController 
PURPOSE: SearchSimilarProductController class is a class uses searchSimilarProduct service query processing function and retrieves all similar product with most similar matching name in order
INVARIANTS: There are no invariants
"""
import numpy as np
from pandas import DataFrame
from services.search_product_service import SearchProductService
from services.search_similar_products_service import SearchSimilarProductsService

class SearchSimilarProductsController:
  """
  NAME: __init__
  PARAMETERS: df, searchSimilarProducts, name
  PURPOSE: injects dependencies to this class
  PRECONDITION: The class is passed it's dependencies via instantiation
  POSTCONDITION: The class is injected searchProduct, df, query dependencies
  """
  def __init__(
    self, 
    df: DataFrame,
    searchSimilarProducts: SearchSimilarProductsService,
    name: str):
      self.df = df
      self.searchSimilarProducts = searchSimilarProducts
      self.name = name

  """
  NAME: execute
  PARAMETERS: none
  PURPOSE: Resolves a user query
  PRECONDITION: The zonal inverted index has been created and both the DataFrame and query are given
  POSTCONDITION: Retrieves all documents with similar names in order 
  """
  def execute(self) -> dict[int, float]:
    """Executes a series of services.
    \n\n returns what its implementation is meant to return"""
    initiate_query_bow, initiate_bow = self.searchSimilarProducts.preprocess(self.df)
    bow, L2_norm_doc = self.searchSimilarProducts.BOW(self.df, initiate_bow)
    query_bow, L2_norm_query = self.searchSimilarProducts.query_BOW(self.name, initiate_query_bow, bow)

    # we multiply length document with length the query and inverse it for cosine similarity
    L2_reciprocal = np.multiply(L2_norm_query,L2_norm_doc)
    L2_product = 1/L2_reciprocal


    query_matrix = query_bow.to_numpy()
    doc_matrix = bow.to_numpy()

    # compute dot product between documents and query
    dot_pdt = np.dot(doc_matrix, query_matrix.T)
    dot_pdt = dot_pdt.flatten()

    # compute cosine similarity
    cos_similarity = np.multiply(dot_pdt, L2_product)

    cos_similarity = cos_similarity.tolist()
    cos_similarity = enumerate(cos_similarity)
    cos_similarity = dict(cos_similarity)
    cos_similarity = dict(sorted(cos_similarity.items(), key = lambda x : x[1], reverse= True))
              
    return cos_similarity

    