# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from models import Pepscrape, db_connect, create_table

class PepScraperPipeline(object):

    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):

        session = self.Session()
        pep = Pepscrape(**item)

        try:
            session.add(pep)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
