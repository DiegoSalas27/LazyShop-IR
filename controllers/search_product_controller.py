from pandas import DataFrame
from services.search_product_service import SearchProductService

class SearchProductController:
  def __init__(
    self, 
    searchProduct: SearchProductService,
    df: DataFrame,
    query: str):
      self.searchProduct = searchProduct
      self.df = df
      self.query = query

  def execute(self) -> tuple[list[int], DataFrame]:
    """Executes a series of services.
    \n\n returns what its implementation is meant to return"""
    all_postings, act_docs = self.searchProduct.query_processing(self.query, self.df)
              
    return all_postings, act_docs

    