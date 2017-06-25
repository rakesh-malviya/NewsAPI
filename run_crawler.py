import scrapy
from scrapy.crawler import CrawlerProcess
from src.newScrap.newScrap.spiders.news_spider import NewsSpider
from src.utils import config

def start_crawler():
  process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
  })
  
  process.crawl(NewsSpider)#,website=config.CRAWL_WEBSITE)
  process.start() 
  
start_crawler()