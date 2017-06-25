import cherrypy
import json
from src.utils import config
from src.utils import myLogger
from src.mongoDB.dbIngestor import Ingestor

import sys
reload(sys)  
sys.setdefaultencoding('utf8')

import os

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return open(config.INDEX_HTML)
   
class StringGeneratorWebService(object):    
    exposed = True
    @cherrypy.tools.accept(media='text/plain')    
    def POST(self, q):                
        answerJSON = self.getQueryAns(q)        
        return answerJSON
        
      
    def getQueryAns(self,query):        
        searchList = self.dbEngine.keywordSearch(query, maxResult=config.MAX_SEARCH_COUNT)
        
        if searchList and len(searchList)>0:
          answerList = []          
          for i,elem in enumerate(searchList):
            tempStr = "Result: "+str(i+1)+"<br>";
            tempStr += "Title: "+str(elem['title'])+"<br>"
            tempStr += 'Url: <a href="%s">%s</a>' %(str(elem['url']),str(elem['url']))            
            answerList.append(tempStr)
            
          answerList.reverse()
          return json.dumps({"answer":answerList})  
            
        else:
          return json.dumps({"answer":["Sorry, no result."]})       
        
        
    
    def __init__(self):
      self.dbEngine = Ingestor()
        
     
    
if __name__ == '__main__':
    conf = {
        'global' : {
                        'server.socket_host' : '0.0.0.0',
                        'server.socket_port' : config.API_PORT,
                        'server.thread_pool' : 8,
                        # interval in seconds at which the timeout monitor runs                        
                    },
        '/': {            
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/generator': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    
    webapp = StringGenerator()
    webapp.generator = StringGeneratorWebService()
    cherrypy.quickstart(webapp, '/', conf)
