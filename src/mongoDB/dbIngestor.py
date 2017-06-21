import newspaper
from src.utils import config
from src.utils.myLogger import dbLogger
from src.utils import loadsave as ls
from pprint import pprint
from pymongo import MongoClient
import pymongo  

class Ingestor:
  def __init__(self):
    client = MongoClient('mongodb://localhost:27017/')
#     client.drop_database(config.DB_NAME);exit()    
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