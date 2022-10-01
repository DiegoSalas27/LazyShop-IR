import sys
# CHANGE IT TO YOUR OWN HOME PATH
sys.path.insert(1, 'C://Users//diego//OneDrive//Escritorio//Desktop//Texas Tech University//Fall-2022//Information retrieval//IR-system//LazyShop-IR')

import time
from domain.models.query_result import QueryResult
from factories.controllers.auto_runners.get_inverted_index_zonal_dictionary_controller_factory import makeGetInvertedIndexZonalDictionaryController
from factories.controllers.queries.search_product_controller_factory import makeSearchProductController

if __name__ == '__main__':
  while True:
    print('creating inverted index')
    inverted_index_zonal_dictionary = makeGetInvertedIndexZonalDictionaryController().execute()
    time_wait = 1440
    print(f'Waiting {time_wait} minutes...')

    # execute queries 
    while True:
      query = input("Enter your query: ")
      if query != '.':
        all_postings: QueryResult = makeSearchProductController(inverted_index_zonal_dictionary, query).execute()
        print({
          'query': all_postings.query,
          'posting_list': all_postings.postingList
        })
      else:
        break

    time.sleep(time_wait * 60) #run program every day