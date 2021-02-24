import scrapy
from scrapy.linkextractors import LinkExtractor

class SouHuSpider(scrapy.Spider):
    name = 'souhu'
    allowed_domains = ['souhu.com']
    start_urls = ['https://www.sohu.com/c/8/1460?spm=smpc.news-home.top-subnav.2.1612186331825O6ASWXp']
    # https://www.sohu.com/a/448102736_123753?spm=smpc.sub-channel.fd-news.1.1612186372933NRFG1kR
    news_url_pattern = r'https://www.sohu.com/a/[0-9]{9}_[0-9]{6}'

    def parse(self, response):
        # title = response.xpath('//*[@id="article-container"]/div[2]/div[1]/div/div[1]/h1').extract()
        # body = response.xpath('//*[@id="mp-editor"]').extract()
        # time = response.xpath('//*[@id="news-time"]').extract()
        # print(title)
        # print(body)
        # print(time)

        link_extractor = LinkExtractor(allow=SouHuSpider.news_url_pattern, )
        links = link_extractor.extract_links(response)
        for link in links:
            # print(link.url, link.text)
            print(link.url)
            # yield scrapy.Request(link.url, callback=self.parse)
