import scrapy
import re
from scrapy.linkextractors import LinkExtractor

from stone_spider.items import NewsItem


class WangYiSpider(scrapy.Spider):
    name = 'wangyi'
    allowed_domains = ['news.163.com']
    start_urls = ['http://news.163.com/special/0001386F/rank_news.html']
    # start_urls = ['https://news.163.com/21/0131/12/G1M19A7K0001899O.html']
    # https://news.163.com/21/0131/23/G1N5KUMC0001899O.html
    news_url_pattern = r'https://news.163.com/[0-9]{2}/[\s\S]*'

    def parse(self, response):

        flag = False
        if re.match(WangYiSpider.news_url_pattern, response.request.url):
            flag = True
        if flag:
            item = NewsItem()
            title = response.xpath('//*[@id="container"]/div[1]/h1/text()').get()
            body = response.xpath('//*[@id="content"]/div[2]').get()
            time = response.xpath('//*[@id="container"]/div[1]/div[2]/text()').get()
            item['title'] = title
            item['body'] = body
            item['time'] = time
            item['source'] = response.request.url
            yield item
            # print(title)
            # print("--------")
            # print("--------")
            # print(body)
            # print("--------")
            # print("--------")
            # print(time)
        # print("current url -> " + response.request.url)
        # print()
        # print()
        # print()

        link_extractor = LinkExtractor(allow=WangYiSpider.news_url_pattern)
        links = link_extractor.extract_links(response)
        for link in links:
            # print(link.url, link.text)
            # print(link.url)
            yield scrapy.Request(link.url, callback=self.parse)
