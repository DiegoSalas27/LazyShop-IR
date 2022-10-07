# LazyShop-IR
This is the Information Retrieval System for Lazy Shop. This system reads from a csv file that contains product details
structured by name, rating, type_of, price, comments which where created by the LazyShop web scraping project. It creates
A Zonal Inverted Index and solve user queries by running linguistic modules from nltk package.

## install dependencies:
```
pip install -r requirements.txt
```

## Run this project:
```
python -m streamlit run main.py
```

## Folder structure:
- controllers: entry point of the system
  - search_product_controller: Entry for point for the search engine. Reads the inverted index and process the query
  - zonal_inverted_index_controller: Entry point for reading csv data and returning inverted index
- services: files in here perform business logic related to LazyShop
  - search_product_service: Implements th search engine by processing queries and returning postings lists
- utils: has utility classes to perform indexation, tokenization and preprocessing of data
    - indexer: implements the indexer functionality and created the zonal inverted index
    - linguistic_modules: implements the linguistic modules functionality and preprocess the query
    - tokenizer: implements the tokenizer functionality and tokenizes the query