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
from services.search_product_service import SearchProductService

# creating a Flask app
app = Flask(__name__)

print('creating inverted index')

inverted_index_zonal_dictionary, df = InvertedIndexZonalDictionaryController().execute()

# on the terminal type: curl http://127.0.0.1:5000/
# enter a query parameter
@app.route('/search', methods = ['GET'])
def home():
  args = request.args
  query = args.get('query')

  # instantiates classes
  searchProduct = SearchProductService(inverted_index_zonal_dictionary)
  all_postings =  SearchProductController(searchProduct, query).execute()
  return jsonify({ 'data': all_postings })

if __name__ == '__main__':
  app.run(debug = True)


