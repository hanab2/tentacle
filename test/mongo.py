import pymongo


# client = pymongo.MongoClient(host='localhost', port=27017)
#
# mapper = client.test
#
# collection = mapper.article
from stone_spider.snowflake import IdWorker

collection = pymongo.MongoClient(host='localhost', port=27017).test.news
generator = IdWorker()
article = {
    "_id": generator.get_id(),
    "title": "test2",
    "body": "body~~~~~"
}

result = collection.insert_one(article)
