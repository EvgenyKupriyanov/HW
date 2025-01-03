# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookparserPipeline:
    # def __init__(self):
    #     client = MongoClient('localhost', 27017)
    #     self.mongobase = client.vacancies231023

    def process_item(self, item, spider):
        print()
        item.get('title')
        collection = []
        collection.append(item)
        print(collection)
        # collection = self.mongobase[spider.title]
        # collection.insert_one(item)
        return item
