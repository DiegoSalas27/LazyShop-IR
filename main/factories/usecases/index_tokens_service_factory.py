from domain.usecases.index_tokens import IndexTokens
from services.usecases.index_tokens_service import IndexTokensService

def makeIndexTokensService() -> IndexTokens:
  return IndexTokensService()