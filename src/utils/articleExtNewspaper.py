"""Get article data from newspaper API"""
import newspaper
from src.utils.myLogger import newsLogger

class NewsPaperEngine():
  
  """Downloads and parses article from given url"""
  def getArticle(self,url):
    article = newspaper.Article(url)
    for i in range(5):  
      article.download()
      print("Retry:",i)
      html = article.html
      if html and len(html)>0:
        break
      
    article.parse()
    article.nlp()
       
    return article
    
  """Returns dictionary of required results given article url"""
  def getArticleData(self,url):
    article = None
    try:
      article = self.getArticle(url)
      if article==None:
        return None
    except Exception as e:
      newsLogger.error("Exception at url:%s Error:%s" %(url,str(e)))
      return None
    
    if article==None:
      return None
    
    if article.html==None or len(article.html)==0:
      return None
    
    if article.text==None or len(article.text)==0:
      return None
    
        
    dataDict = {}
    
    dataDict["authors"] = article.authors 
    
    if(article.publish_date):
      dataDict["publish_date"] = article.publish_date 
    else:
      #Probably not a news Article
      return None
      
    dataDict["title"] = article.title
    dataDict["keywords"] = article.keywords
    dataDict["text"] = article.text
    dataDict["url"] = article.url
        
    return dataDict

   
