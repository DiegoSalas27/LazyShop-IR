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
  
  @staticmethod
  def stem(sentence_doc: list[str]) -> LiteralString:
    """stems all words in doc and joins the stemmed tokens back into a sentence for further procesing
    \n\n returns the stemmed tokens as a sentence for further processing"""
    # stems all words in doc
    sentence_str_1 = [p_stemmer.stem(word_tk) for word_tk in sentence_doc]  # list[str,]
    # joins the stemmed tokens back into a sentence for further procesing
    sentence_str_1 = " ".join(sentence_str_1) # str

    return sentence_str_1

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

  @staticmethod
  def modify_tokens(sentence_doc: list[str]) -> list[str]:
    """process the given string performing replacements using business logic and deleting stop-words 
    \n\n returns the replaced senteced without stop-words"""
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