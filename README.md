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