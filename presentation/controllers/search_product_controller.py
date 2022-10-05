from pandas import DataFrame
from domain.usecases.search_product import SearchProduct
from domain.models.query_result import QueryResult
from presentation.protocols.controller import Controller

class SearchProductController(Controller):
  def __init__(
    self, 
    searchProduct: SearchProduct,
    df: DataFrame,
    query: str):
      self.searchProduct = searchProduct
      self.df = df
      self.query = query

  def execute(self) -> tuple[list[int], DataFrame]:
    all_postings, act_docs = self.searchProduct.query_processing(self.query, self.df)
              
    return all_postings, act_docs

    