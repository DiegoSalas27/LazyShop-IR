from infrastructure.nltk.nltk_adapter import NltkAdapter
from domain.usecases.search_product import SearchProduct
from services.usecases.search_product_service import SearchProductService

def makeSearchProductService(inverted_index_zonal_dictionary: dict[str, dict]) -> SearchProduct:
  nlUtil = NltkAdapter()
  return SearchProductService(nlUtil, inverted_index_zonal_dictionary)