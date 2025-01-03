import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from scrapy.utils import response
from pictureparser.items import PictureparserItem


class UnsplashSpider(scrapy.Spider):
    name = "unsplash"
    allowed_domains = ["unsplash.com"]


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f'https://unsplash.com/s/photos/{kwargs.get('query')}']

    def parse(self, response:HtmlResponse):
        links = response.xpath("//div[@class='lWLQX']//a[@class='mG0SP']")
        for link in links:
            yield response.follow(link, callback=self.parse_pic)

        print()
        pass
    def parse_pic(self, response:HtmlResponse):
        print()
        # name = response.xpath("//h1/text()").get()
        # text = response.xpath("//p[@class='F7hSb']/text()").get()
        # url = response.url
        # photo = response.xpath("//div[@class='xH5KD']/img[2]/@srcset").get().split(' ')[0]
        # yield (PictureparserItem(name=name, text=text, url=url, photo=photo))
        loader = ItemLoader(item=PictureparserItem(), response=response)
        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('text', "//p[@class='F7hSb']/text()")
        loader.add_value('url', response.url)
        loader.add_xpath('photo', "//div[@class='xH5KD']/img[2]/@srcset")

        yield loader.load_item()