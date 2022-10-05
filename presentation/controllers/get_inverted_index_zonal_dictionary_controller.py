from typing import Any
from domain.constants import terms_dictionary_for_zone
from domain.usecases.index_tokens import IndexTokens
from domain.usecases.modify_tokens import ModifyTokens
from domain.usecases.read_csv import ReadCsv
from domain.usecases.tokenize import Tokenize
from presentation.protocols.controller import Controller
from services.usecases.read_csv_service import ReadCsvService

class GetInvertedIndexZonalDictionaryController(Controller):
  def __init__(
    self, 
    read_csv: ReadCsv,
    tokenizer: Tokenize, 
    linguistic_modules: ModifyTokens, 
    indexer: IndexTokens):
      self.read_csv = read_csv
      self.tokenizer = tokenizer
      self.linguistic_modules = linguistic_modules
      self.indexer = indexer

  def execute(self) -> Any:
    df = self.read_csv.read_csv("walmart-products-modified.csv", 'latin1')

    for zone in df.columns:
        # only doing indexing for the chosen zones above
        if zone in terms_dictionary_for_zone.keys():
            # saving docID and the row content for the chosen zones
            for docID, doc in enumerate(df[zone]): # int, str; list[(int, str), ]
              sentence_doc = self.tokenizer.tokenize(doc)
              modified_tokens = self.linguistic_modules.modify_tokens(sentence_doc)
              self.indexer.build_inverted_index(zone, docID, modified_tokens)
              
    return terms_dictionary_for_zone

    