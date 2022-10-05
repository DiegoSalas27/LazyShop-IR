from domain.usecases.search_product import SearchProduct
from domain.models.query_result import QueryResult
from presentation.protocols.controller import Controller

class SearchProductController(Controller):
  def __init__(
    self, 
    searchProduct: SearchProduct,
    query: str):
      self.searchProduct = searchProduct
      self.query = query

  def execute(self) -> QueryResult:
    all_postings = self.searchProduct.query_processing(self.query)
              
    return all_postings

    