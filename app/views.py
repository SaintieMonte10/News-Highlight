from flask import render_template,redirect,url_for
from app import app
from .requests import get_sources, get_articles

# Views
@app.route('/')
@app.route('/sources')
def news_sources():
    '''
    View root page function that returns the index page and its data
    '''
    news_sources = get_sources()
    return render_template('sources.html', news_sources=news_sources)


@app.route('/articles/<source>')
def news_articles(source):
    '''
    View news page function that returns the news details page and its data
    '''
    news_articles = get_articles(source)
    return render_template('articles.html', news_articles=news_articles)