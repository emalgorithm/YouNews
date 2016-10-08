import requests

NEWS_API_KEY               = '2a6d71a6686245cebf684a570d0c7a7'
NEWS_API_ARTICLES_ENDPOINT = 'https://newsapi.org/v1/articles'
NEWS_API_SOURCES_ENDPOINT  = 'https://newsapi.org/v1/sources'

def get_latest_articles(source_id):
    params = { 'source': source_id,
               'apiKey': NEWS_API_KEY,
               'sortBy': 'latest',
             }

    r = requests.get(NEWS_API_ARTICLES_ENDPOINT, params=params)
    return r.json()