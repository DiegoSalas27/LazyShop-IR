from typing import Any
from services.protocols.nl_util import NlUtil
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
p_stemmer = PorterStemmer()
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

# this adapter class that implements the Natural Langue Util interface
class NltkAdapter(NlUtil):

  def word_tokenizer(self, rowString: str) -> list[str]:
    return word_tokenize(rowString)

  def word_stemmer(self, word: str) -> str:
    return p_stemmer.stem(word)

  def stop_words(self) -> set:
    return stop_words

  def edit_distance(self, queryTerm: str, dictionaryTerm: str) -> Any:
    return nltk.edit_distance(queryTerm, dictionaryTerm)