from typing import List

# This is the model that will be retrieved by the sytem as result of the query
class QueryResult:
  def __init__(self, query: str, postingList: List[int]):
    self.query = query
    self.postingList = postingList