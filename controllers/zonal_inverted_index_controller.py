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
from utils.tokenizer import Tokenizer
from utils.linguistic_modules import LinguisticModules
from utils.indexer import Indexer

class InvertedIndexZonalDictionaryController: 
  """
  NAME: __init__
  PARAMETERS: name
  PURPOSE: injects dependencies to this class
  PRECONDITION: The class is passed it's dependencies via instantiation
  POSTCONDITION: The class is injected name dependencies
  """
  def __init__(
    self, 
    name: str):
      self.name = name
  """
  NAME: execute
  PARAMETERS: none
  PURPOSE: Creation of zonal inverted index
  PRECONDITION: A name parameter is given to get the corresponding csv file
  POSTCONDITION: Retrieves a zonal inverted index used for ranking and cosine similarity
  """
  def execute(self) -> tuple[dict[str, dict], pd.DataFrame]: 
    """Executes a series of services.
    \n\n returns what its implementation is meant to return"""
    df = pd.read_csv(self.name, encoding='latin1')

    terms_dictionary_for_zone = {
            'name': { },
            'type_of': { },
            'comments': { }
            }
    for zone in df.columns:
        # only doing indexing for the chosen zones above
        if zone in terms_dictionary_for_zone.keys():
            # saving docID and the row content for the chosen zones
            for docID, doc in enumerate(df[zone], 1): # int, str; list[(int, str), ]
                
                # tokenises the words in the row of the selected zone based on NLTK vocab
                sentence_doc = Tokenizer.tokenize(str(doc))
                # stems all words in doc
                modified_tokens = LinguisticModules.modify_tokens(sentence_doc)

                for term in modified_tokens: # 'str'
                    # for each zone the term increased in doc freq and appends the posting list if term exists
                        if term in terms_dictionary_for_zone[zone]: # previously from this doc or other docs
                            # print(term, terms_dictionary_for_zone[zone], type(terms_dictionary_for_zone[zone][term][1]))
                            if docID in terms_dictionary_for_zone[zone][term][1].keys(): # previously from this doc
                                org_val = terms_dictionary_for_zone[zone][term][1][docID]
                                terms_dictionary_for_zone[zone][term][1].update({docID : org_val+1})
                            else: # from other docs
                                terms_dictionary_for_zone[zone][term][1].update({docID : 1})
                                terms_dictionary_for_zone[zone][term][0] += 1
                                
                        # if term doesnt exist, put doc freq as 1 and append the first posting list
                        else: # previously non-existant
                            terms_dictionary_for_zone[zone][term] =[[],{}] # list[[int], [int, ]]; list[[doc freq], [docIds,]]
                            terms_dictionary_for_zone[zone][term][0] = 1 # int; doc freq
                            terms_dictionary_for_zone[zone][term][1].update({docID : 1})

    return terms_dictionary_for_zone, df
    