"""
Solved Issue of Date not found for bbc by adding 
{'attribute': 'class', 'value': 'date date--v2', 'content': 'data-datetime'},
to PUBLISH_DATE_TAGS of newspaper.extractor API
"""

from src.mongoDB.dbIngestor import Ingestor
dbEngine = Ingestor()

badDateList = []
badAuthorList = []
badTitleList = []
badKeywordsList = []
badTextList = []
badUrlList = []

cursor = dbEngine.article_collection.find()

for elem in cursor:
  date = elem['publish_date']
  authorList = elem['authors']
  title= elem["title"]
  keywords=elem["keywords"]
  text=elem["text"]
  url=elem["url"]
  
  if date==None:
    badDateList.append(url)
    
  if authorList==None or len(authorList)==0:
    badAuthorList.append(url)
    
  if title==None or len(title)==0:
    badTitleList.append(url)
    
  if keywords==None or len(keywords)==0:
    badKeywordsList.append(url)
    
  if text==None or len(text)==0:
    print(keywords)
    badTextList.append(url)
    
  if url==None or len(url)==0:
    badUrlList.append(url)
    
print("badAuthorList",len(badAuthorList))
print("badDateList",len(badDateList),badDateList)
print("badTitleList",len(badTitleList))
print(len(badKeywordsList))
print(len(badTextList))
print(len(badUrlList))

from src.utils.articleExtNewspaper import NewsPaperEngine
newsEngine = NewsPaperEngine()

for url in badDateList:
  print(url)
  article = newsEngine.getArticle(url)
  if article.html==None or len(article.html)==0:
    print("Error html is None")
    continue
  
  print(article.clean_doc)
  print(article.publish_date)
