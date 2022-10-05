from infrastructure.nltk.nltk_adapter import NltkAdapter
from domain.usecases.search_product import SearchProduct
from infrastructure.pandas.pandas_adapter import PandasAdapter
from main.factories.usecases.modify_tokens_service_factory import makeModifyTokensService
from main.factories.usecases.tokenize_service_factory import makeTokenizeService
from services.usecases.search_product_service import SearchProductService

def makeSearchProductService(inverted_index_zonal_dictionary: dict[str, dict]) -> SearchProduct:
  nlUtil = NltkAdapter()
  tokenizer = makeTokenizeService()
  linguistic_modules = makeModifyTokensService()
  fileManager = PandasAdapter()

  return SearchProductService(nlUtil, inverted_index_zonal_dictionary, tokenizer, linguistic_modules, fileManager)