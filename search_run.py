from src.mongoDB.dbIngestor import Ingestor
from pprint import pprint
dbEngine = Ingestor()
# pprint(dbEngine.article_collection.find_one({"url":"http://www.bbc.com/news/uk-40357280"}))
dbEngine.keywordSearch("Grenfell Tower survivors")
