"""
AUTHOR: P Shiva Kumar / Diego Salas Noain
FILENAME: indexer.py
SPECIFICATION: 
  - We need to construct an inverted index by zones to solve queries
  - We create a doctionary (zonal inverted index)
  - We should be able to retrieve efficiently the data based on a given zone much quicker
FOR: CS 5364 Information Retrieval Section 001 
"""

"""
NAME: Indexer 
PURPOSE: Indexer class is a utility class that contains a build_inverted_index method that creates a zonal inverted index
INVARIANTS: There are no invariants
"""

from constants import terms_dictionary_for_zone

# this class implements the indexer
class Indexer:
  """
  NAME: build_inverted_index
  PARAMETERS: zone, docID, modified_tokens
  PURPOSE: creates a zonal inverted index
  PRECONDITION: Zone and docID are given, the data has been preprocessed
  POSTCONDITION: This function should return an updated dictionary
  """
  @staticmethod
  def build_inverted_index(zone: str, docID: int, modified_tokens: list[str]) -> dict[str, dict]:
    """Builds the inverted index based on the modified tokens from the linguistic modules
    \n\n returns the inverted index dictionary"""
    for term in modified_tokens: # 'str'
      # for each zone the term increased in doc freq and appends the posting list if term exists
      if term in terms_dictionary_for_zone[zone]: # previously from this doc or other docs
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
          # print(type(terms_dictionary_for_zone[zone][term][1]))
    # return the inverted-index dictionary
    return terms_dictionary_for_zone
      