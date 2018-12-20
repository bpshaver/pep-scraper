# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from pep_scraper.items import PepScraperItem

class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['python.org']
    start_urls = ['https://www.python.org/dev/peps/']

    def parse(self, response):
        """ Parses the Python PEP main page for links to each PEP's individual
        page, then yields a request for that page.

        @url https://www.python.org/dev/peps/
        @returns items 0 0
        @returns requests 10
        """
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
        """ Parses the page for an individual Python PEP. 

        # @url https://www.python.org/dev/peps/pep-0484/
        # @returns items 1 1
        # @returns requests 0 0
        # @scrapes PEP Title Author url

        # This contract will fail since page_parse is run in isolation,
        # and the Item passed through in the meta dict is missing. There
        # is no easy way around this for now. 
        # Takeaway: Contracts work only for the top-level parse function,
        # unless callbacks can be run in isolation.
        """
        item = response.meta['item']

        soup = BeautifulSoup(response.text, 'lxml')

        table = soup.find('tbody')
        for row in table.find_all('tr'):
            try:
                key = row.find('th').text.rstrip(':').replace('-','_')
                item[key] =  row.find('td').text
            except KeyError as e:
                print(f"Unexpected key: {key}")

        yield item
