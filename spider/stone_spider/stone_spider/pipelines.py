# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import pymongo
from markdownify import markdownify
from dateutil.parser import parse
from stone_spider.date_extractor import DateExtractor
from stone_spider.snowflake import IdWorker


class StoneSpiderPipeline:
    __id_generator = IdWorker()
    __collection = pymongo.MongoClient(host='localhost', port=27017).sentiment.news

    def process_item(self, item, spider):
        if item:
            self.rinseBody(item)
            self.rinseTime(item)
            # print("++++++++++++++++++++++++++")
            # print(item)
            news = {
                "_id": self.getID(),
                "title": item.get("title"),
                "body": item.get("body"),
                "source": item.get("source"),
                "time": item.get("time")
            }
            StoneSpiderPipeline.__collection.insert_one(news)
        return item

    def getID(self):
        return StoneSpiderPipeline.__id_generator.get_id()

    def rinseBody(self, item):
        item['body'] = markdownify(item.get('body'))

    def rinseTime(self, item):
        time_string = DateExtractor.extract(str(item['time']))
        # # 先转换为时间数组
        # time_array = time.strptime(time_string, "%Y-%m-%d %H:%M")
        # # 转换为时间戳
        # time_stamp = int(time.mktime(time_array))
        # item['time'] = time_stamp * 1000
        item['time'] = parse(time_string)
