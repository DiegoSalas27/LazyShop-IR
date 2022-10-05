from factories.usecases.search_product_service_factory import makeSearchProductService
from presentation.controllers.search_product_controller import SearchProductController
from presentation.protocols.controller import Controller

def makeSearchProductController(inverted_index_zonal_dictionary: dict[str, dict], query: str) -> Controller:
  searchProduct = makeSearchProductService(inverted_index_zonal_dictionary)

  return SearchProductController(searchProduct, query)