# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider

def writeFile(url):
  with open("urlFile.txt","a+") as urlFile:
    urlFile.write(url+'\n') 
    
#

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

print(list(set(bad_keys)))

class NewsSpider(CrawlSpider):
  
    # The name of the spider
    name = "newsSpiderExtract"

    # The domains that are allowed (links to other domains are skipped)
    allowed_domains = ["bbc.com"]

    # The URLs to start with
#     start_urls = ["http://www.bbc.com/"]
    start_urls = ["http://www.bbc.com/news/uk-40356303"]

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
      
        dateStr = response.xpath("//*[contains(@class, 'date--v2')]/text()").extract_first()
        print(response.url)
        print(dateStr)
        exit()

        items = []

        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
        
        for link in links:
            for allowed_domain in self.allowed_domains:              
                if allowed_domain in link.url:
                  print("URL:",link.url)
                  writeFile(link.url)
        
