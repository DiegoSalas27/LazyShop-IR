# This is the model that will be retrieved by the sytem as result of the query
class QueryResult:
  """Returns a response that can be used by the database"""
  def __init__(self, query: str, postingList: list[int]):
    self.query = query
    self.postingList = postingList