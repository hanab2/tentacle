import markdown
from bs4 import BeautifulSoup

from mapper.news_mapper import find_one_news, update_one_news
from nlp.service.location_service import service_location_discovery
from nlp.service.segment_service import service_word_cloud
from nlp.service.sentiment_service import service_sentiment

__location_filter = {'location': {'$exists': False}}
__sentiment_filter = {'sentiment': {'$exists': False}}
__segment_filter = {
    'segment': {'$exists': False},
    'segment_error': {'$exists': False}
}
__finished_filter = {
    'location': {'$exists': True},
    'sentiment': {'$exists': True},
    'segment': {'$exists': True},
    'status': {'$exists': False}
}


def mine_news(condition_filter=None) -> dict:
    return find_one_news(condition_filter=condition_filter)


def location_process():
    news = mine_news(__location_filter)
    if news:
        location = service_location_discovery(news.get('body'))
        update_one_news(news['_id'], {'$set': {'location': location}})


def sentiment_process():
    news = mine_news(__sentiment_filter)
    if news:
        sentiment = service_sentiment(news.get('body'))
        update_one_news(news['_id'], {'$set': {'sentiment': sentiment}})


def segment_process():
    news = mine_news(__segment_filter)
    if news:
        try:
            html = markdown.markdown(news.get('body'))
            soup = BeautifulSoup(html, 'html.parser')
            service_word_cloud(soup.getText(), news.get('time'))
            update_one_news(news['_id'], {'$set': {'segment': True}})
        except Exception as e:
            update_one_news(news['_id'], {'$set': {'segment_error': True}})


def status_process():
    news = mine_news(__finished_filter)
    if news:
        update_one_news(news['_id'], {'$set': {'status': 1}})
    print(news)


if __name__ == '__main__':
    pass
