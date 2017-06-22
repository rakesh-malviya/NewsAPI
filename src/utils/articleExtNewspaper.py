import newspaper

def getArticle(url):
  article = newspaper.Article(url)
  for i in range(5):  
    article.download()
    print("Retry:",i)
    html = article.html
    if html and len(html)>0:
      break
    
  article.parse()
  
#   print("HTML:::  ",article.html[:10])     
#   print("authors",article.authors)
#   print("publish_date",article.publish_date)  
#   print("title",article.title)
#   print("is_media_news",article.is_media_news())
#   print("top_image",  article.top_image)
#   print("movies",article.movies)
  
  article.nlp()
     
#   print("keywords",article.keywords)
#   print("summary",article.summary)
  
  return article

def getArticleData(url):
  
  article = getArticle(url)
  dataDict = {
    "authors":article.authors,
    "publish_date":article.publish_date,  
    "title":article.title,     
    "keywords":article.keywords,
    "text":article.text,
    "url":url
  }
  
  return dataDict

# print(getArticleData("http://www.bbc.com/news/world-latin-america-40325944"))

   
