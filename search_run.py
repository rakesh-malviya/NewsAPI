# -*- coding: utf-8 -*-

from src.mongoDB.dbIngestor import Ingestor
from pprint import pprint
from src.utils import config
dbEngine = Ingestor()
# dbEngine.keywordSearch("Grenfell Tower survivor")
while True:
    try:
        query = raw_input('Enter Search Keywords > ')
        if len(query)==0:
          break
        dbEngine.keywordSearch(query,maxResult=config.MAX_SEARCH_COUNT)
    except EOFError:
        break

