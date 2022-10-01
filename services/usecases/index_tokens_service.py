from domain.usecases.index_tokens import IndexTokens
from domain.constants import terms_dictionary_for_zone

# this class implements the index_tokens interface
class IndexTokensService(IndexTokens):

  def build_inverted_index(self, zone: str, docID: int, modified_tokens: list[str]) -> dict[str, dict]:
    for term in modified_tokens: # 'str'
      # for each zone the term increased in doc freq and appends the posting list if term exists
      if term in terms_dictionary_for_zone[zone]:
          terms_dictionary_for_zone[zone][term][0] += 1 # int; doc freq
          terms_dictionary_for_zone[zone][term][1].append(docID) # list[int,]
      # if term doesnt exist, put doc freq as 1 and append the first posting list
      else:
          terms_dictionary_for_zone[zone][term] =[[],[]] # list[[int], [int, ]]; list[[doc freq], [docIds,]]
          terms_dictionary_for_zone[zone][term][0] = 1 # int; doc freq
          terms_dictionary_for_zone[zone][term][1].append(docID)

    return terms_dictionary_for_zone
      