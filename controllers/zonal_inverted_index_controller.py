"""
AUTHOR: P Shiva Kumar / Diego Salas Noain
FILENAME: zonal_inverted_index_controller.py
SPECIFICATION: 
  - Need to have a point of entry for creating the zonal inverted index
  - Create a controller class that can do that work
FOR: CS 5364 Information Retrieval Section 001 
"""

"""
NAME: InvertedIndexZonalDictionaryController 
PURPOSE: InvertedIndexZonalDictionaryController class is a class that executes a series steps to build an inverted zonal index
INVARIANTS: There are no invariants
"""

import pandas as pd
from constants import terms_dictionary_for_zone
from utils.tokenizer import Tokenizer
from utils.linguistic_modules import LinguisticModules
from utils.indexer import Indexer

class InvertedIndexZonalDictionaryController: 
  """
  NAME: execute
  PARAMETERS: none
  PURPOSE: Creates a zonal inverted index
  PRECONDITION: No precondition
  POSTCONDITION: Retrieves an zonal inverted index by updating the terms_dictionary_for_zone dictionary and retrieves the df for further use
  """
  def execute(self) -> tuple[dict[str, dict], pd.DataFrame]: 
    """Executes a series of services.
    \n\n returns what its implementation is meant to return"""
    df = pd.read_csv("walmart-products-detail.csv", encoding='latin1')

    for zone in df.columns:
        # only doing indexing for the chosen zones above
        if zone in terms_dictionary_for_zone.keys():
            # saving docID and the row content for the chosen zones
            for docID, doc in enumerate(df[zone]): # int, str; list[(int, str), ]
              sentence_doc = Tokenizer.tokenize(str(doc))
              modified_tokens = LinguisticModules.modify_tokens(sentence_doc)
              Indexer.build_inverted_index(zone, docID + 1, modified_tokens)
              
    return terms_dictionary_for_zone, df

    