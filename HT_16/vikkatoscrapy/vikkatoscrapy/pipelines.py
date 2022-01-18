# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3


class NewsPipeline:
    def open_spider(self, spider):
        self.con = sqlite3.connect('vikkatoscrapy/news.sqlite')
        self.cur = self.con.cursor()

    def process_item(self, item, spider):
        if self.is_unique_record(item['url']):
            request = 'INSERT INTO news (title, content, tags, url, full_date) VALUES (?, ?, ?, ?, ?)'
            self.cur.execute(request, (item.get('title'), item.get('content'),
                                       item.get('tags'), item.get('url'), spider.date))

    def is_unique_record(self, url):
        request = 'SELECT * FROM news WHERE url=:url'
        result = self.cur.execute(request, {'url': url}).fetchone()
        return result is None

    def close_spider(self, spider):
        self.con.commit()
        self.con.close()




