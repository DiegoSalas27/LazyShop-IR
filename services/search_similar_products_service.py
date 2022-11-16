"""
AUTHOR: P Shiva Kumar / Diego Salas Noain
FILENAME: search_product_service.py
SPECIFICATION: 
  - We need to resolve the user's query
  - We should be able to di this by passing the query to linguistic modules and correcting errors
FOR: CS 5364 Information Retrieval Section 001 
"""

"""
NAME: SearchProductService 
PURPOSE: SearchProductService class is a class that executes a series of steps to process a query given by the user
INVARIANTS: There are no invariants
"""

import numpy as np
from numpy import linalg as LA
import itertools
from utils.tokenizer import Tokenizer
from utils.linguistic_modules import LinguisticModules
from pandas import DataFrame
import pandas as pd
from constants import terms_dictionary_for_zone

# this class implements the search engine
class SearchSimilarProductsService:
  """
  NAME: __init__
  PARAMETERS: inverted_index_zonal_dictionary
  PURPOSE: injects dependencies to this class
  PRECONDITION: The class is passed it's dependencies via instantiation
  POSTCONDITION: The class is injected inverted_index_zonal_dictionary dependency
  """
  def __init__(self, inverted_index_zonal_dictionary: dict[str, dict]):
      self.inverted_index_zonal_dictionary = inverted_index_zonal_dictionary,

  def query_BOW(self, name: str, q_bow: DataFrame, bow: DataFrame) -> tuple[DataFrame, float]:
    sentence_doc = Tokenizer.tokenize(str(name))
    modified_query = LinguisticModules.modify_tokens(sentence_doc)

    for term in modified_query: # 'str'
      # for each zone the term increased in doc freq and appends the posting list if term exists
      if term in bow.columns:
          q_bow.loc[0, term] += 1
    
    L2_norm_query = LA.norm(q_bow.to_numpy())
    return q_bow, L2_norm_query

  def BOW(self, doc_database: DataFrame, bow: DataFrame) -> tuple[DataFrame, list]:
    L2_norm_doc = []
    for zone in doc_database.columns:
      # only doing indexing for the chosen zones above
      if zone in terms_dictionary_for_zone.keys():
        # saving docID and the row content for the chosen zones
        for docID, doc in enumerate(doc_database[zone]): # int, str; list[(int, str), ]
          # tokenises the words in the row of the selected zone based on NLTK vocab
          sentence_doc = Tokenizer.tokenize(str(doc))
          modified_query = LinguisticModules.modify_tokens(sentence_doc)

          for term in modified_query: # 'str'
            # for each zone the term increased in doc freq and appends the posting list if term exists
            if term in bow.columns:
                bow.loc[docID, term] += 1
          L2_norm_doc.append(LA.norm(bow.loc[docID, :].to_numpy()))
                      
    return bow, L2_norm_doc
  """
  NAME: _edit_distance
  PARAMETERS: query_terms, posting_list, each_term
  PURPOSE: Calculates the distance of a term by using levenshtein distance to a given dictionary term
  PRECONDITION: query_terms is not empty
  POSTCONDITION: posting_list is updated by being appended the appropiate documents to retrieve
  """
  def preprocess(self, df: DataFrame) -> tuple[DataFrame, DataFrame]: # private method
    # Cosine similarity
    zero_data = np.zeros(shape=(1,len(self.inverted_index_zonal_dictionary[0]['name'].keys())))
    initiate_query_bow = pd.DataFrame(zero_data, columns = self.inverted_index_zonal_dictionary[0]['name'].keys())
    
    zero_data = np.zeros(shape=(len(df),len(self.inverted_index_zonal_dictionary[0]['name'].keys())))
    initiate_bow = pd.DataFrame(zero_data, columns = self.inverted_index_zonal_dictionary[0]['name'].keys())

    return initiate_query_bow, initiate_bow
  """
  NAME: _compute_higest_priority
  PARAMETERS: posting_list
  PURPOSE: Returns the postings list in order of priority based on AND and OR queries.
  PRECONDITION: posting_list is not empty. The function is called after we have our postings lists.
  POSTCONDITION: postings list of high and low priority are retrieved.
  """
  def doc_scoring(self, term_freq: dict, doc_freq: list[int], df: DataFrame) -> dict:
    score = {}
    doc_score = {}
    for key, val in term_freq.items():
      for i in range(0, len(val), 1):
        if key not in score.keys():
          tf_idf = (1 + np.log10(val[i])) * (np.log10(df.shape[0]/doc_freq[i]))
          if tf_idf > -9999:
            score.update({key : [tf_idf]})
          else:
            score.update({key : [0]})
        else:
          tf_idf = (1 + np.log10(val[i])) * (np.log10(df.shape[0]/doc_freq[i]))
          if tf_idf > -9999:
            score[key].append(tf_idf)
          else:
            score[key].append(0)
  
    for key, val in score.items():
      doc_score.update({key : sum(val)})


    return dict(sorted(doc_score.items(), key = lambda x : x[1], reverse= True))

  """
  NAME: query_processing
  PARAMETERS: query, df
  PURPOSE: Orchestrates through helper methods and utility classes to process the user's query
  PRECONDITION: a query is given and a dataframe is given.
  POSTCONDITION: postings list of high and low priority are combined and returned
  """
  def tf_df(self, posting_list: list[dict]) ->  tuple[dict, list[int]]:
    """Search for a product based given a query string using an inverted index
    \n\n returns a tuple"""
    # for multiple query terms, we also get (OR query)
    posting_list_combined = set(list(itertools.chain(*posting_list))) # list[int, ]

    ### tf|term,doc
    term_freq_given_doc_term = {}
    for docID in posting_list_combined:
      for i in range(0, len(posting_list), 1):
        if docID not in term_freq_given_doc_term.keys():
          if docID not in posting_list[i]:
            term_freq_given_doc_term.update({docID : [0]})
          else:
            term_freq_given_doc_term.update({docID : [posting_list[i][docID]]})
        else:
          if docID not in posting_list[i]:
            term_freq_given_doc_term[docID].append(0)
          else:
            term_freq_given_doc_term[docID].append(posting_list[i][docID])
    
    
    ### df|term
    doc_freq_given_terms = []
    for i in range(0, len(posting_list), 1):
      doc_freq_given_terms.append(len(posting_list[i]))


    return term_freq_given_doc_term, doc_freq_given_terms