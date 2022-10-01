from domain.usecases.tokenize import Tokenize
from infrastructure.nltk.nltk_adapter import NltkAdapter
from services.usecases.tokenize_service import TokenizeService

def makeTokenizeService() -> Tokenize:
  nlUtil = NltkAdapter()
  return TokenizeService(nlUtil)