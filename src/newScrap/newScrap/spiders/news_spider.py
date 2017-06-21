# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
# import sys,os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from src.utils.myLogger import newsLogger
from src.utils import articleExtNewspaper as aen
from tldextract import extract
from src.mongoDB import dbIngestor  

def writeFile(url):
  with open("urlFile.txt","a+") as urlFile:
    urlFile.write(url+'\n')     
    


bad_keys = ['shop', 'cookies', 'register', 'help', 'search', 'twitter', 'terms-of-use', 
            'linkedin', 'subscribe', 'jobs', 'newsletter', 'archive', 'feedback', 
            'preferences', 'friendster', 'privacy', 'browse', 'myspace', 'charts', 
            'legal', 'advert', 'maps', 'board', 'academy', 'developer', 'mail', 
            'donate', 'events', 'careers', 'profile', 'tickets', 'product', 'terms', 
            'purchase', 'stop', 'signup', 'faq', 'howto', 'privacy-policy', 'facebook', 
            'plus', 'account', 'password', 'site-map', 'coupons', 'subscription', 'info', 
            'stumbleupon', 'about', 'flickr', 'forum', 'admin', 'vimeo', 'bebo', 'how to', 
            'youtube', 'itunes', 'mobile', 'siteindex', 'contact', 'services', 'store', 
            'imgur', 'login', 'shopping', 'sitemap', 'proxy']

class NewsSpider(CrawlSpider):
    # The name of the spider
    name = "newsSpiderExtract"
    
    def __init__(self, website='http://www.bbc.com', *args, **kwargs):
      super(NewsSpider, self).__init__(*args, **kwargs)
      self.website = website
      self.start_urls = [website]
      self.dbIngestor = dbIngestor.Ingestor()
      
      # Get domain from tldextract API
      extractResult = extract(website) 
      allowed_domain = extractResult[1]+"."+extractResult[2]
      
      # The domains that are allowed (links to other domains are skipped)
      self.allowed_domains = [allowed_domain]
      
      newsLogger.info("Website: "+website)
      newsLogger.info("Allowed Domain: "+ allowed_domain)
      
    # rule: extract all (unique and canonicalized) links and parse them using the parse_items method
    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse_items"
        )
    ]


    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)


    def parse_items(self, response):
        items = []

        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
        
        for link in links:
            index = link.url.rfind('/')
            linkUrlPart = link.url[:index]
            if any(x in linkUrlPart for x in bad_keys):
              continue
            for allowed_domain in self.allowed_domains:              
                if allowed_domain in linkUrlPart:
                  writeFile(link.url)
                  articleData = self.extract_article_info(link.url)
                  if len(articleData['keywords'])!=0 :
                    self.insert_article_data_db(articleData)
                  
                                                      
                  
    def insert_article_data_db(self,dataDict):
      self.dbIngestor.insert_one(dataDict)
      
                  
    def extract_article_info(self,url):
      dataDict = aen.getArticleData(url)
      dataDict['website'] = self.website
      return dataDict