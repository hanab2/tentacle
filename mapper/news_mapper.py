from mapper.config import client

news_collection = client.sentiment.news


def insert_one_news(news: dict):
    news_collection.insert_one(news)


def update_one_news(document_id, field: dict):
    news_collection.update_one(filter={'_id': document_id}, update=field, upsert=True)


def find_one_news(condition_filter=None):
    return news_collection.find_one(filter=condition_filter)


if __name__ == '__main__':
    res = find_one_news()
    print(res, type(res))
