"""
AUTHOR: P Shiva Kumar / Diego Salas Noain
FILENAME: main.py
SPECIFICATION: 
  - This file instantiates the main classes: InvertedIndexZonalDictionaryController and SearchProductController (with their dependencies)
  - Previous to the query, the zonal inverted index is created
  - When the query is processed, the zonal inverted index is used by the SearchProductController which will use a service to resolve the query
FOR: CS 5364 Information Retrieval Section 001 
"""
import os
dirpath = os.getcwd()
import sys
sys.path.insert(1, dirpath)
import streamlit as st
from controllers.zonal_inverted_index_controller import InvertedIndexZonalDictionaryController
from controllers.search_product_controller import SearchProductController
from services.search_product_service import SearchProductService

if __name__ == '__main__':
  print('creating inverted index')

  inverted_index_zonal_dictionary, df = InvertedIndexZonalDictionaryController().execute()

  # execute queries 

  st.header("Walmart: Search for items") # Display text in header formatting.

  query = st.text_input("Type here", "Spider") # Display a single-line text input widget.

  # instantiates classes
  searchProduct = SearchProductService(inverted_index_zonal_dictionary)
  all_postings, act_docs =  SearchProductController(searchProduct, df, query).execute()

  # Write arguments to the app.
  st.write('items:\n',act_docs)
  st.write('postings list: \n', all_postings)