from app import app
import urllib.request,json
from .models import NewsSource,NewsArticle

# Getting api key
api_key = app.config["NEWS_API_KEY"]

# Getting the news base url
news_sources_url = app.config["SOURCES_API_URL"]

#Getting articles URL
news_articles_url = app.config["ARTICLES_API_URL"]

def process_sources(sources_list):
    all_sources = []

    for source in sources_list:
        new_source = NewsSource(source['id'], source['name'])
        all_sources.append(new_source)

    return all_sources

def process_articles(articles_list):
    all_articles = []

    for article in articles_list:
        new_article = NewsArticle(
            article['title'],
            article['description'],
            article['urlToImage'],
            article['publishedAt'],
            article['content']
        )
        all_articles.append(new_article)

    return all_articles

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    sources_url = news_sources_url.format(api_key)

    with urllib.request.urlopen(sources_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        source_results = None
        if get_news_response['sources']:
            sources = get_news_response['sources']
            source_results = process_sources(sources)

    return source_results

def get_articles(source):
    """  """
    articles_url = news_articles_url.format(source, api_key)

    with urllib.request.urlopen(articles_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        article_results = None
        if get_news_response['articles']:
            articles = get_news_response['articles']
            article_results = process_articles(articles)

    return article_results
