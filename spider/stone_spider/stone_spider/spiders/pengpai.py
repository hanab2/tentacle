import scrapy


class PengpaiSpider(scrapy.Spider):
    name = 'thepaper'
    allowed_domains = ['thepaper.cn']
    start_urls = ['https://www.thepaper.cn/newsDetail_forward_11028828']

    def parse(self, response):
        title = response.xpath('/html/body/div[3]/div[1]/div[1]/h1').extract()
        body = response.xpath('/html/body/div[3]/div[1]/div[1]/div[3]').extract()
        time = response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/p[2]/text()').extract()
        print(title)
        print(body)
        print(time)



        nextUrl = response.xpath('/html/body/div[3]/div[1]/div[1]/div[12]/div[1]/div[2]/a').extract()
        print(nextUrl)
