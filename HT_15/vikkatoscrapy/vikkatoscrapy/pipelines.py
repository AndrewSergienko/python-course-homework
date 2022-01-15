# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter


class NewsPipeline:
    def process_item(self, item, spider):
        if spider.csv_exporter_start_flag:
            self.exporter.export_item(item)
        else:
            self.file = open(f'{spider.date.replace("/", "_")}.csv', 'ab')
            self.exporter = CsvItemExporter(self.file)
            self.exporter.fields_to_export = ['title', 'content', 'tags', 'url']
            self.exporter.start_exporting()
            self.exporter.export_item(item)
            spider.csv_exporter_start_flag = True
        return item

    def spider_closed(self):
        self.exporter.finish_exporting()
        self.file.close()