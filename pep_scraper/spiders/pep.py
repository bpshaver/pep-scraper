# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from pep_scraper.items import PepScraperItem

class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['python.org']
    start_urls = ['https://www.python.org/dev/peps/']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        num_index = soup.find('div', attrs={'id':'numerical-index'}).find('tbody')

        for row in num_index.find_all('tr'):
            item = PepScraperItem()
            values = [td for td in row.find_all('td')]

            item['short_typ'] = values[0].text,
            item['short_num'] = values[1].text,
            item['short_tit'] = values[2].text,
            item['short_aut'] = values[3].text,
            item['url'] = 'https://www.python.org' + values[1].find('a')['href']

            request = scrapy.http.Request(item['url'],
                callback=self.page_parse, meta={'item':item})

            yield request

    def page_parse(self, response):
        item = response.meta['item']

        soup = BeautifulSoup(response.text, 'lxml')

        table = soup.find('tbody')
        for row in table.find_all('tr'):
            try:
                key = row.find('th').text.rstrip(':').replace('-','_')
                item[key] =  row.find('td').text
            except KeyError as e:
                print(f"Unexpected key: {key}")

        # print('-----')
        # print(item)
        # print('-----')

        yield item
