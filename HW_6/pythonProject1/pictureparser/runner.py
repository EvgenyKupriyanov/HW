import twisted
from scrapy.crawler import CrawlerProcess
from scrapy.utils.reactor import install_reactor
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from pictureparser.spiders.unsplash import UnsplashSpider
from pictureparser.items import PictureparserItem
from scrapy.utils import response

if __name__ == '__main__':
    configure_logging()
    install_reactor(twisted.internet.asyncioreactor.AsyncioSelectorReactor)
    process = CrawlerProcess(get_project_settings())
    process.crawl(UnsplashSpider, query='мотоциклы')
    process.start()