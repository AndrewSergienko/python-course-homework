import re
from datetime import datetime

import scrapy
from bs4 import BeautifulSoup

from vikkatoscrapy.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = 'news'

    def start_requests(self):
        urls = [
            'https://www.vikka.ua/'
        ]
        for url in urls:
            self.date = self.select_date()
            yield scrapy.Request(url=f"{url}{self.date}/", callback=self.parse)

    def select_date(self):
        while True:
            date = input('Введіть дату, новини якої потрібно показати у форматі: yyуу/mm/dd: ')
            if self.is_valid_date(date):
                break
            else:
                print('Неправильна дата.')
        return date

    def is_valid_date(self, date_str):
        check_result = re.sub(r'\d{4}/\d{2}/\d{2}', '', date_str)
        if len(check_result) == 0:
            now = datetime.now()
            date = datetime(*map(int, date_str.split('/')))
            return date <= now
        return False

    def parse(self, response, **kwargs):
        soup = BeautifulSoup(response.text, 'lxml')
        news_list = soup.select_one('.cat-posts-wrap')
        for news in news_list:
            info_url = news.select_one('.title-cat-post a').get('href')
            yield scrapy.Request(url=info_url, callback=self.parse_news_info)

    def parse_news(self, news):
        info_url = news.select_one('.title-cat-post a')
        yield scrapy.Request(url=info_url, callback=self.parse_news_info)

    def parse_news_info(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        content = soup.select_one('.entry-content')
        tags_ul = soup.select_one('.entry-tags ul')

        url = response.url
        title = soup.select_one('.post-title').text
        text = content.get_text(separator='\n')
        tags = ', '.join([f'#{tag.get_text()}' for tag in tags_ul])

        yield NewsItem(title=title, content=text, tags=tags, url=url)
