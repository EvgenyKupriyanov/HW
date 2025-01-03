import scrapy
from scrapy.http import HtmlResponse

from bookparser.items import BookparserItem


class LitresSpider(scrapy.Spider):
    name = "litres"
    allowed_domains = ["litres.ru"]
    start_urls = ["https://www.litres.ru/new/"]

    def parse(self, response):
        next_page = response.xpath("//li[@class='Paginator_arrow__SAzJS']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath("//a[@data-testid='art__title']/@href").getall()
        for link in links:
           yield response.follow(link, callback=self.book_parse)


    def book_parse(self, response: HtmlResponse):
        title = response.xpath("//h1/text()").get()
        price = response.xpath("//strong[@class='SaleBlock_block__price__default__MitcJ']/text()").get()
        url = response.url
        yield BookparserItem(title=title, price=price, url=url)
        print()