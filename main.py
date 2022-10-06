import sys
# CHANGE IT TO YOUR OWN HOME PATH
sys.path.insert(1, 'C://Users//diego//OneDrive//Escritorio//Desktop//Texas Tech University//Fall-2022//Information retrieval//IR-system//LazyShop-IR')
import streamlit as st
from controllers.zonal_inverted_index_controller import InvertedIndexZonalDictionaryController
from controllers.search_product_controller import SearchProductController
from services.search_product_service import SearchProductService

if __name__ == '__main__':
  print('creating inverted index')

  inverted_index_zonal_dictionary, df = InvertedIndexZonalDictionaryController().execute()

  # execute queries 

  st.header("Walmart: Search for items")

  query = st.text_input("Type here", "Spider")
  searchProduct = SearchProductService(inverted_index_zonal_dictionary)
  all_postings, act_docs =  SearchProductController(searchProduct, df, query).execute()

  st.write('items:\n',act_docs)
  st.write('postings list: \n', all_postings)