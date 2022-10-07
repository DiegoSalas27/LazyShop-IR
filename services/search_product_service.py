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


import itertools
from utils.tokenizer import Tokenizer
from utils.linguistic_modules import LinguisticModules
from pandas import DataFrame
import nltk
import pandas as pd

# this class implements the search engine
class SearchProductService:
  """
  NAME: __init__
  PARAMETERS: inverted_index_zonal_dictionary
  PURPOSE: injects dependencies to this class
  PRECONDITION: The class is passed it's dependencies via instantiation
  POSTCONDITION: The class is injected inverted_index_zonal_dictionary dependency
  """
  def __init__(self, inverted_index_zonal_dictionary: dict[str, dict]):
      self.inverted_index_zonal_dictionary = inverted_index_zonal_dictionary,

  """
  NAME: _edit_distance
  PARAMETERS: query_terms, posting_list, each_term
  PURPOSE: Calculates the distance of a term by using levenshtein distance to a given dictionary term
  PRECONDITION: query_terms is not empty
  POSTCONDITION: posting_list is updated by being appended the appropiate documents to retrieve
  """
  def _edit_distance(self, query_terms: list[str], posting_list: list[int], each_term: int): # private method
    for term in query_terms[:]: # str     
      # for individual terms compute edit distance with each term in the 'name' inverted-index dictionary
      # this is useful if there is a typo in one or multiple of the query terms
      edit_dist_list = [[key, nltk.edit_distance(term, key)]  for key in self.inverted_index_zonal_dictionary[0]['name']] # list[[str, double], ]
      edit_dist_list_1 = list(zip(*edit_dist_list)) # list[(str,)(double,)]
      # choose the min edit distance as the closest term match in the inverted-index dictionary
      if min(edit_dist_list_1[1]) >=2:
          print('No matching results')
          return 0, 0
      # choose the min edit distance as the closest term match in the inverted-index dictionary
      internal_query = edit_dist_list_1[0][edit_dist_list_1[1].index(min(edit_dist_list_1[1]))] # str

      # from the term matched in the inverted-index, append, its posting list to 'posting-list'
      posting_list.append(list(self.inverted_index_zonal_dictionary[0]['name'][internal_query][1])) # list[[int, ], ]
      each_term +=1

  """
  NAME: _compute_higest_priority
  PARAMETERS: posting_list
  PURPOSE: Returns the postings list in order of priority based on AND and OR queries.
  PRECONDITION: posting_list is not empty. The function is called after we have our postings lists.
  POSTCONDITION: postings list of high and low priority are retrieved.
  """
  def _compute_higest_priority(self, posting_list: list[int]) -> tuple[list[int], list[int]]: # private method
    # for mutltiple query terms, the highest priority posting lists are ones which has ALL the terms in the query (AND query) 
    if posting_list:
        posting_list_combined_for_and_high_priority = set.intersection(*map(set, posting_list)) # set[int, ]
        posting_list_combined_for_and_high_priority = list(posting_list_combined_for_and_high_priority) # list[int, ]
    else:
        posting_list_combined_for_and_high_priority = []

    # for multiple query terms, we also get (OR query)
    posting_list_combined = list(itertools.chain(*posting_list)) # list[int, ]
    posting_list_combined_for_or_low_priority = set(posting_list_combined) # set[int, ]
    posting_list_combined_for_or_low_priority = list(posting_list_combined_for_or_low_priority)

    return posting_list_combined_for_and_high_priority, posting_list_combined_for_or_low_priority, 

  """
  NAME: query_processing
  PARAMETERS: query, df
  PURPOSE: Orchestrates through helper methods and utility classes to process the user's query
  PRECONDITION: a query is given and a dataframe is given.
  POSTCONDITION: postings list of high and low priority are combined and returned
  """
  def query_processing(self, query: str, df: DataFrame) ->  tuple[list[int], DataFrame]:
    """Search for a product based given a query string using an inverted index
    \n\n returns a tuple"""

    if query == ' ' or query == '':
      return None, None

    posting_list: list[int] = [] # list[]
    each_term = 0 # int

    sentence_doc = Tokenizer.tokenize(str(query))
    modified_query = LinguisticModules.modify_tokens(sentence_doc)

    res = self._edit_distance(modified_query, posting_list, each_term)

    if res != None and res[0] == 0 and res[1] == 0:
      return 0, 0

    posting_list_combined_for_and_high_priority, posting_list_combined_for_or_low_priority = self._compute_higest_priority(posting_list)

    # we append the OR query after the AND query as OR is deemed as lower priority here
    for docID_low_priority in posting_list_combined_for_or_low_priority: # int
        if docID_low_priority not in posting_list_combined_for_and_high_priority:
            posting_list_combined_for_and_high_priority.append(docID_low_priority) # list[int,]

     # return the posting list from above
    act_docs = pd.DataFrame(df.loc[posting_list_combined_for_and_high_priority])
    for docID_of_cur_term in posting_list_combined_for_and_high_priority:
        print(pd.DataFrame(df.loc[docID_of_cur_term]))
    if len(act_docs) == 0:
      return "Sorry there are no results for your search", 0
    return posting_list_combined_for_and_high_priority, act_docs


    
      