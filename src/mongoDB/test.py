import newspaper
from src.utils import config
from src.utils.myLogger import dbLogger
from src.utils import loadsave as ls
from pprint import pprint


urlList = [
           u'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/',
           u'http://www.cnn.com/2013/11/27/justice/tucson-arizona-captive-girls/',
           u'http://www.cnn.com/2013/12/11/us/texas-teen-dwi-wreck/index.html',
           u'http://edition.cnn.com/2017/05/02/asia/india-maoist-rebels-villagers/index.html',
           u'http://edition.cnn.com/2017/06/18/sport/pakistan-india-champions-trophy-cricket/index.html',
           u'http://edition.cnn.com/2017/06/19/design/healthcare-clinic-designs/index.html',
           u'http://edition.cnn.com/2017/06/12/politics/9th-circuit-travel-ban/index.html',
           u'http://edition.cnn.com/2017/06/19/us/coming-out-as-mormon-and-gay-trnd/index.html',
           u'http://edition.cnn.com/2017/06/19/politics/supreme-court-partisan-gerrymandering/index.html',
           u'http://edition.cnn.com/2017/06/19/health/colorado-preteen-smartphone-initiative/index.html',
           u'http://edition.cnn.com/2017/06/19/asia/indonesia-bali-prison-break/index.html',
           u'http://edition.cnn.com/2017/06/20/us/weather-west-heat-wave/index.html',
           u'http://money.cnn.com/2017/06/19/news/india/jet-airways-baby-born-flight-free-tickets/index.html',
           u'http://edition.cnn.com/2017/06/19/weather/antarctica-melt-texas-rain-climate-change-trnd/index.html'
           u'http://edition.cnn.com/2017/06/20/world/world-refugee-day-worst-crisis-in-history/index.html',
           u'http://edition.cnn.com/2017/06/19/us/exoplanets-nasa-kepler-announcement/index.html',
           u'http://money.cnn.com/2017/06/19/news/economy/brexit-talks-uk-eu/index.html',
           u'http://edition.cnn.com/2017/06/19/arts/marlene-dietrich-dressed-for-the-image/index.html',
           u'http://edition.cnn.com/travel/article/montreal-bagel-wars/index.html',
           u'http://edition.cnn.com/travel/article/south-africa-hotel-silo/index.html',
           u'http://edition.cnn.com/2017/06/19/opinions/brexit-meets-reality-cleppe-opinion/index.html',
           u'http://edition.cnn.com/2017/06/19/opinions/syria-escalation-russia-lemmon-opinion/index.html',
           u'http://edition.cnn.com/2017/06/19/opinions/terrorism-polarization-opinion-bergen/index.html'           
           ]


ls.save_obj(urlList, "urlList")

def getArticle(url):
  article = newspaper.Article(url)
  for i in range(20):  
    article.download()
    print("Retry:",i)
    html = article.html
    if html and len(html)>0:
      break  
  
  print("HTML:::  ",article.html[:10])
  article.parse()   
  print("authors",article.authors)
  print("publish_date",article.publish_date)  
  print("title",article.title)
  print("is_media_news",article.is_media_news())
  print("top_image",  article.top_image)
  print("movies",article.movies)
  article.nlp()   
  print("keywords",article.keywords)
  print("summary",article.summary)
  return article
#   print("text",article.text)
  
# artList = []
#  
# for url in urlList:
#   artList.append(getArticle(url))
# ls.save_obj(artList,"artList")  

# getArticle("http://www.bbc.com/news/business-40340875")
# getArticle("http://www.bbc.com/capital/story/20170620-how-to-get-ahead-in-the-era-of-the-show-off")
#  
# exit()

import newspaper
from src.utils.myLogger import dbLogger 

# dbLogger.info("Build news source")
# cnn_paper = newspaper.Source("http://cnn.com/")
# print("Size:",cnn_paper.size())
# cnn_paper.build()
# # cnn_paper = newspaper.build("http://cnn.com/")
#  
# dbLogger.info("Check news source")
# for article in cnn_paper.articles:
#   print(article)



# getArticle(url)
from pymongo import MongoClient
import pymongo  

class Ingestor:
  def __init__(self):
    client = MongoClient('mongodb://localhost:27017/')
    client.drop_database(config.DB_NAME);exit()    
    self.db = client[config.DB_NAME]
    self.article_collection = self.db[config.DB_ART_COLLECTION]
        
    try:
      self.article_collection.create_index([("url", pymongo.ASCENDING)],unique=True)
      self.article_collection.create_index([("keywords", pymongo.TEXT)])
      self.article_collection.create_index([("title", pymongo.TEXT)])
      self.article_collection.create_index([("text", pymongo.TEXT)])                  
    except Exception as e:
      pass    
    
  def insert_one(self,dataDict):
    try:
      post_id = self.article_collection.insert_one(dataDict).inserted_id    
      return post_id
    except pymongo.errors.DuplicateKeyError as e:
      dbLogger.info("Duplicate URL:"+str(dataDict['url']))
      
    
  
  def keywordSearch(self,query,maxResult=5):
    if query and len(query)>0:
      searchGen =  self.article_collection.find({'$text': {'$search': query}})
    else:
      searchGen =  self.article_collection.find()
    searchList = []
    
    for i,elem in enumerate(searchGen):
      if i==maxResult:
        break;
      
      searchList.append(elem)
      
    for i,elem in enumerate(searchList):
      print("\nResult: "+str(i))
      print("Title: "+str(elem['title']))
      print("Url: "+str(elem['url']))
      print("Keywords: "+str(elem['keywords']))
    
    
dbIng = Ingestor()
# dbIng.keywordSearch("supreme attacker isis")
dbIng.keywordSearch("",maxResult=100)
artList = ls.load_obj("artList")
print(len(artList)) 
for article in artList:
  dataDict = {
    "authors":article.authors,
    "publish_date":article.publish_date,  
    "title":article.title,     
    "keywords":article.keywords,
    "summary":article.summary,
    "text":article.text,
    "url":article.url
  }
#   print("keywords",article.keywords)
#   print("date",article.publish_date)    
#   print("title",article.title)
  dbIng.insert_one(dataDict)