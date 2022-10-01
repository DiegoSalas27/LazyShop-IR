import sys

sys.path.insert(1, 'C://Users//diego//OneDrive//Escritorio//Desktop//Texas Tech University//Fall-2022//Information retrieval//IR-system//LazyShop-IR')
from factories.usecases.index_tokens_service_factory import makeIndexTokensService
from factories.usecases.modify_tokens_service_factory import makeModifyTokensService
from factories.usecases.read_csv_service_factory import makeReadCsvService
from factories.usecases.tokenize_service_factory import makeTokenizeService
from presentation.controllers.auto_runners.get_inverted_index_zonal_dictionary_controller import GetInvertedIndexZonalDictionaryController
from presentation.protocols.controller import Controller


def makeGetInvertedIndexZonalDictionaryController() -> Controller:
  read_csv_service = makeReadCsvService()
  tokenizer = makeTokenizeService()
  linguistic_modules = makeModifyTokensService()
  indexer = makeIndexTokensService()

  return GetInvertedIndexZonalDictionaryController(read_csv_service, tokenizer, linguistic_modules, indexer)