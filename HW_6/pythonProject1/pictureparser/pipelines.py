# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from typing import Any

import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.media import MediaPipeline, FileInfoOrError


class PictureparserPipeline:
    def process_item(self, item, spider):
        print()
        return item

class PPP(ImagesPipeline):
    def get_media_requests(
        self, item: Any, info: MediaPipeline.SpiderInfo
    ) -> list[Request]:
        if item['photo']:
            for img in item['photo']:
                try:
                    yield scrapy.Request(img)
                except Exception as e:
                    print(e)
    # def item_completed(
    #     self, results: list[FileInfoOrError], item: Any, info: MediaPipeline.SpiderInfo
    # ) -> Any:
    #     print()
    #     if results:
    #         item['photo'] = [itm[1] for itm in results if itm[0]]
    #     return item