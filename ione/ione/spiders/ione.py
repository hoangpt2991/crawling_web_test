import scrapy
from crawler.items import CrawlerItem
from scrapy.selector import Selector
class IoneWeb(scrapy.Spider):
    name = "ione"
    allowed_domains=['https://ione.net/']
    start_urls=['https://ione.net/']


    def parse(self, response):
        print('================>Start to crawling the URL' + response.url)
        links =  Selector(response).xpath("//div[@class='title-news']/a/@href").extract()
        for link in links:
            url = CrawlerItem()
            url['title_link']=link.css('title::text').get()
            url['author_link']=link.css('.fck_detail strong::text').get()
            url['publish_time']=link.css('.date::text').get()
            yield url
        