from factories.usecases.search_product_service_factory import makeSearchProductService
from presentation.protocols.controller import Controller
from presentation.controllers.queries.search_product_controller import SearchProductController

def makeSearchProductController(inverted_index_zonal_dictionary: dict[str, dict], query: str) -> Controller:
  searchProduct = makeSearchProductService(inverted_index_zonal_dictionary)

  return SearchProductController(searchProduct, query)