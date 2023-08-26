# LazyShop-IR
This is the Information Retrieval System for Lazy Shop. This system reads from a csv file that contains product details
structured by name, rating, type_of, price, comments which where created by the LazyShop web scraping project. It creates
A Zonal Inverted Index and solve user queries by running linguistic modules from nltk package.

Once the Zonal Inverted Index is created, LazyShop IR solves client queries that look for products by name with the following logic:
1. query processing:
    * tokenizing words
    * modifying tokens by stemming them, and performing various replacements using regex patterns and deleting stop-words
    * edit ditance using levenshtein distance to account for typos in que given query
    * return posting list
2. term frequencey and document frequency is calculated
3. documents are scored based of term and document frequency using tf-idf. Postings list are returned in order of priority.

When a client clicks on a product the same or the most similar product from other stores are retrieved using cosine similarity in order for the client to compare prices. In order to do this, the following steps take place:
1. dataframes from bag of words are created
2. caculate document bag of words for cosine similarity
3. cosine similarity is calculated and the most similar product (if a the same product is found in different stores, it will be retrieved as it is a exact match) is retrieved.

## install dependencies:
```
pip install -r requirements.txt
```

## Run this project:
```
python -m streamlit run main.py
```
