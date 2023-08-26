"""
AUTHOR: P Shiva Kumar / Diego Salas Noain
FILENAME: linguistic_modules.py
SPECIFICATION: 
  - We need to preprocess the data
  - We create a utility class that can perform linguistic modules operations
  - We should retrieve normlized terms ready for indexing
FOR: CS 5364 Information Retrieval Section 001 
"""

"""
NAME: LinguisticModules 
PURPOSE: LinguisticModules class is a utility class that preprocess the data by stemming, string replacement with regex deleting stop words
INVARIANTS: There are no invariants
"""

import re
from string import punctuation
from utils.tokenizer import Tokenizer
import nltk
from nltk.stem.porter import PorterStemmer
p_stemmer = PorterStemmer()
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from typing_extensions import LiteralString

# this class implements the linguistic modules
class LinguisticModules:
  """
  NAME: stem
  PARAMETERS: sentence_doc
  PURPOSE: stems all words in doc and joins the stemmed tokens back into a sentence for further procesing
  PRECONDITION: a sentence is given as a list of strings
  POSTCONDITION: returns the stemmed tokens as a sentence for further processing
  """
  @staticmethod
  def stem(sentence_doc: list[str]) -> LiteralString:
    """stems all words in doc and joins the stemmed tokens back into a sentence for further procesing
    \n\n returns the stemmed tokens as a sentence for further processing"""
    # stems all words in doc
    sentence_str_1 = [p_stemmer.stem(word_tk) for word_tk in sentence_doc]  # list[str,]
    # joins the stemmed tokens back into a sentence for further procesing
    sentence_str_1 = " ".join(sentence_str_1) # str

    return sentence_str_1

  """
  NAME: string_replacement
  PARAMETERS: sentence_doc
  PURPOSE: process the given string performing replacements using regex patterns 
  PRECONDITION: the given sentence was stemmed. This function is called after the given stence was stemmed
  POSTCONDITION: returns the replaced stemmed sentenced by using regex patterns
  """
  @staticmethod
  def string_replacement(sentence_doc: list[str]) -> str: # private method
    """process the given string performing replacements using regex patterns 
    \n\n returns the replaced stemmed sentenced"""
    stemmed_sentence = LinguisticModules.stem(sentence_doc)
    # subs all symbols/punctuations (including space) with a space (' '); excludes digits
    replaced_str = re.sub(r'\W+', ' ', stemmed_sentence)
    # subs all digits with a space (' '); a sequence of digits (without space) is given one (' ')
    replaced_str = re.sub(r'\d+', ' ', replaced_str)
    # subs all symbols AND digits (including spaces) with a space (' '); includes digits
    replaced_str = re.sub(r'[^a-zA-Z]', ' ', replaced_str)
    # compiles a pattern and subs out the pattern in sentence_str_1 with ' '
    replaced_str = re.compile('(\s*)pron(\s*)').sub(' ', replaced_str)

    return replaced_str

  """
  NAME: modify_tokens
  PARAMETERS: sentence_doc
  PURPOSE: process the given string performing replacements using business logic and deleting stop-words
  PRECONDITION: the given sentence was stemmed and replaced by regex patterns. This function is called after the sentence has been stemmed and replaced by regex patterns
  POSTCONDITION: returns the replaced sentece without stop-words
  """
  @staticmethod
  def modify_tokens(sentence_doc: list[str]) -> list[str]:
    """process the given string performing replacements using business logic and deleting stop-words 
    \n\n returns the replaced sentece without stop-words"""
    replaced_string = LinguisticModules.string_replacement(sentence_doc)

    # tokenize to clean up one more time if 're' has introduced and garbage
    tokenized_words = Tokenizer.tokenize(replaced_string) # list[str,]
    # strip removes whitespace at beginning and end of string (not in between)
    modified_tokens = [str(word_tk_1).strip() for word_tk_1 in tokenized_words] # list[str,]
    # strings with >=2 chars only
    modified_tokens  = [word_str for word_str in modified_tokens if len(word_str) >= 2] # list[str,]
    # strings which are not symbols/punctuations
    modified_tokens = [word_str for word_str in modified_tokens  if word_str not in punctuation]
    # strings which are not stop-words; check with: Spacy_Eng.vocab['word'].is_stop
    modified_tokens = [word_str for word_str in modified_tokens if word_str not in stop_words]


    return modified_tokens