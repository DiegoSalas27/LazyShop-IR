import pandas as pd
from constants import terms_dictionary_for_zone
from utils.tokenizer import Tokenizer
from utils.linguistic_modules import LinguisticModules
from utils.indexer import Indexer

class InvertedIndexZonalDictionaryController:
  def execute(self) -> tuple[dict[str, dict], pd.DataFrame]: 
    """Executes a series of services.
    \n\n returns what its implementation is meant to return"""
    df = pd.read_csv("walmart-products-modified.csv", encoding='latin1')

    for zone in df.columns:
        # only doing indexing for the chosen zones above
        if zone in terms_dictionary_for_zone.keys():
            # saving docID and the row content for the chosen zones
            for docID, doc in enumerate(df[zone]): # int, str; list[(int, str), ]
              sentence_doc = Tokenizer.tokenize(str(doc))
              modified_tokens = LinguisticModules.modify_tokens(sentence_doc)
              Indexer.build_inverted_index(zone, docID, modified_tokens)
              
    return terms_dictionary_for_zone, df

    