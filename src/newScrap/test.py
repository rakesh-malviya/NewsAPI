import tldextract

def test(url):
  index = url.rfind('/')
  url = url[:index]
  print(url)
  extract = tldextract.extract(url) 
  print(extract[2]) 
  print(extract)


test("https://account.bbc.com/account?ptrt=http%3A%2F%2Fwww.bbc.com%2F")
test("http://www.bbc.com/news/world/middle_east")
test("http://www.bbc.com/news/live/business-40300846")
import re
url = "http://www.bbc.com/news/live/business-40300846"
url = "http://www.bbc.com/cbbc"
index = url.rfind('/')
linkUrlPart = url[:index]
linkUrlPartEnd = url[index+1:]
if linkUrlPartEnd and len(linkUrlPartEnd):
  #Remove special characters  
  linkUrlPartEnd = re.sub(r'[^A-Za-z0-9]', ' ', linkUrlPartEnd)
  linkUrlPartEndList = linkUrlPartEnd.split()
  print(linkUrlPartEndList)