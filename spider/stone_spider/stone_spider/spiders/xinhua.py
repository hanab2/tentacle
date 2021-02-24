import scrapy
from scrapy.linkextractors import LinkExtractor

class SouhuSpider(scrapy.Spider):
    name = 'xinhua'
    allowed_domains = ['xinhuanet.com']
    start_urls = ['http://xinhuanet.com/']

    news_url_pattern = r'https://news.163.com/[0-9]{2}/[\s\S]*'

    def parse(self, response):
        link_extractor = LinkExtractor(allow=(r'subject/\d+/$',), )
        links = link_extractor.extract_links(response)
        print(links)
        for link in links:
            # print(link.url, link.text)
            print(link.url)
