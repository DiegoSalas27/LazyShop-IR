import itertools

from pandas import DataFrame
from domain.models.query_result import QueryResult
from domain.usecases.modify_tokens import ModifyTokens
from domain.usecases.search_product import SearchProduct
from domain.usecases.tokenize import Tokenize
from services.protocols.file_manager import FileManager
from services.protocols.nl_util import NlUtil

# this class implements the search engine interface
class SearchProductService(SearchProduct):
  def __init__(
    self, 
    nlUtil: NlUtil, 
    inverted_index_zonal_dictionary: dict[str, dict],
    tokenizer: Tokenize, 
    linguistic_modules: ModifyTokens, 
    fileManager: FileManager):
    self.nlUtil = nlUtil
    self.inverted_index_zonal_dictionary = inverted_index_zonal_dictionary,
    self.tokenizer = tokenizer
    self.linguistic_modules = linguistic_modules
    self.fileManager = fileManager

  def _edit_distance(self, query_terms: list[str], posting_list: list[int], each_term: int): # private method
    for term in query_terms[:]: # str       
      # for individual terms compute edit distance with each term in the 'name' inverted-index dictionary
      # this is useful if there is a typo in one or multiple of the query terms
      edit_dist_list = [[key, self.nlUtil.edit_distance(term, key)]  for key in self.inverted_index_zonal_dictionary[0]['name']] # list[[str, double], ]
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

  def _compute_higest_priority(self, posting_list: list[int]) -> tuple[list[int], list[int]]: # private method
    # for mutltiple query terms, the highest priority posting lists are ones which has ALL the terms in the query (AND query) 
    posting_list_combined_for_and_high_priority = set.intersection(*map(set, posting_list)) # set[int, ]
    posting_list_combined_for_and_high_priority = list(posting_list_combined_for_and_high_priority) # list[int, ]

    # for multiple query terms, we also get (OR query)
    posting_list_combined = list(itertools.chain(*posting_list)) # list[int, ]
    posting_list_combined_for_or_low_priority = set(posting_list_combined) # set[int, ]
    posting_list_combined_for_or_low_priority = list(posting_list_combined_for_or_low_priority)

    return posting_list_combined_for_and_high_priority, posting_list_combined_for_or_low_priority, 

  def query_processing(self, query: str, df: DataFrame) ->  tuple[list[int], DataFrame]:
    if query == '':
      return None, None

    posting_list: list[int] = [] # list[]
    each_term = 0 # int

    sentence_doc = self.tokenizer.tokenize(str(query))
    modified_query = self.linguistic_modules.modify_tokens(sentence_doc)

    res = self._edit_distance(modified_query, posting_list, each_term)
    if res != None and res[0] == 0 and res[1] == 0:
      return 0, 0

    posting_list_combined_for_and_high_priority, posting_list_combined_for_or_low_priority = self._compute_higest_priority(posting_list)

    # we append the OR query after the AND query as OR is deemed as lower priority here
    for docID_low_priority in posting_list_combined_for_or_low_priority: # int
        if docID_low_priority not in posting_list_combined_for_and_high_priority:
            posting_list_combined_for_and_high_priority.append(docID_low_priority) # list[int,]

    # return the posting list from above
    act_docs = self.fileManager.access_group(df, posting_list_combined_for_and_high_priority) 
    for docID_of_cur_term in posting_list_combined_for_and_high_priority:
        print(self.fileManager.access_group(df, docID_of_cur_term))
    return posting_list_combined_for_and_high_priority, act_docs


    
      