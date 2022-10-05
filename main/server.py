import sys
# CHANGE IT TO YOUR OWN HOME PATH
sys.path.insert(1, 'C://Users//diego//OneDrive//Escritorio//Desktop//Texas Tech University//Fall-2022//Information retrieval//IR-system//LazyShop-IR')
import time
import streamlit as st
from main.factories.controllers.get_inverted_index_zonal_dictionary_controller_factory import makeGetInvertedIndexZonalDictionaryController
from main.factories.controllers.search_product_controller_factory import makeSearchProductController
from domain.models.query_result import QueryResult

if __name__ == '__main__':
  print('creating inverted index')
  inverted_index_zonal_dictionary, df = makeGetInvertedIndexZonalDictionaryController().execute()
  time_wait = 1440
  print(f'Waiting {time_wait} minutes...')

  # execute queries 

  st.header("Walmart: Search for items")

  query = st.text_input("Type here", "Spider")
  all_postings, act_docs = makeSearchProductController(inverted_index_zonal_dictionary, df, query).execute()

  st.write('items:\n',act_docs)
  st.write('postings list: \n', all_postings)