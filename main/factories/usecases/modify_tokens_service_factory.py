from domain.usecases.modify_tokens import ModifyTokens
from infrastructure.nltk.nltk_adapter import NltkAdapter
from services.usecases.modify_tokens_service import ModifyTokensService

def makeModifyTokensService() -> ModifyTokens:
  nlUtil = NltkAdapter()
  return ModifyTokensService(nlUtil)