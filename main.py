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
from flask import Flask, jsonify, request
from controllers.zonal_inverted_index_controller import InvertedIndexZonalDictionaryController
from controllers.search_product_controller import SearchProductController
from controllers.search_similar_products_controller import SearchSimilarProductsController
from services.search_product_service import SearchProductService
from services.search_similar_products_service import SearchSimilarProductsService

# creating a Flask app
app = Flask(__name__)

print('creating inverted index')

inverted_index_zonal_dictionary, df = InvertedIndexZonalDictionaryController('walmart-products-detail.csv').execute()
inverted_index_zonal_dictionary_second, df_2 = InvertedIndexZonalDictionaryController('target_new_479products.csv').execute()

# on the terminal type: curl http://127.0.0.1:5000/
# enter a query parameter
@app.route('/search', methods = ['GET'])
def home():
  args = request.args
  query = args.get('query')

  # instantiates classes
  searchProduct = SearchProductService(inverted_index_zonal_dictionary)
  searchSimilarProducts = SearchSimilarProductsService(inverted_index_zonal_dictionary)
  all_postings =  SearchProductController(df, searchProduct, searchSimilarProducts, query).execute()
  return jsonify({ 'data': all_postings }) # returns top 10 products based on tf-idf

@app.route('/similarity', methods = ['GET'])
def getProductsByName():
  args = request.args
  name = args.get('name')
  
  # instantiates classes
  searchSimilarProducts = SearchSimilarProductsService(inverted_index_zonal_dictionary_second)
  all_postings =  SearchSimilarProductsController(df_2, searchSimilarProducts, name).execute()
  return jsonify({ 'data': list(all_postings.keys())[0:1] })

if __name__ == '__main__':
  app.run(debug = True)

