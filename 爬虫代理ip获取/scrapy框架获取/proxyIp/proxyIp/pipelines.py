# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ProxyipPipeline(object):
    def process_item(self, item, spider):
        f = open("ipss.py", "a+")
        f.write(str(item) + ',\n')
        return item