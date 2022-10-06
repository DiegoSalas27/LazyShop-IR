from constants import terms_dictionary_for_zone

# this class implements the indexer
class Indexer:

  @staticmethod
  def build_inverted_index(zone: str, docID: int, modified_tokens: list[str]) -> dict[str, dict]:
    """Builds the inverted index based on the modified tokens from the linguistic modules
    \n\n returns the inverted index dictionary"""
    for term in modified_tokens: # 'str'
      # for each zone the term increased in doc freq and appends the posting list if term exists
      if term in terms_dictionary_for_zone[zone]:
          terms_dictionary_for_zone[zone][term][0] += 1 # int; doc freq
          terms_dictionary_for_zone[zone][term][1].append(docID) # list[int,]
      # if term doesnt exist, put doc freq as 1 and append the first posting list
      else:
          terms_dictionary_for_zone[zone][term] = [[],[]] # list[[int], [int, ]]; list[[doc freq], [docIds,]]
          terms_dictionary_for_zone[zone][term][0] = 1 # int; doc freq
          terms_dictionary_for_zone[zone][term][1].append(docID)

    return terms_dictionary_for_zone
      