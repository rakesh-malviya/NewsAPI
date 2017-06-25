import ConfigParser
import os
import json
configFileLoc = "config/newsAPI.cfg"

API_PORT = None
DB_NAME  = None
DB_ART_COLLECTION = None
MONGODB_URL= None
CRAWL_WEBSITE = None
INDEX_HTML=None
MAX_SEARCH_COUNT = None
try:
    if not os.path.exists(configFileLoc):
        print "No configuration file found. " + '\n'
        raise Exception('Config File not found')
    else:
        configParser = ConfigParser.RawConfigParser()
        configParser.read(configFileLoc)
        API_PORT = int(configParser.get('config', 'API_PORT'))
        INDEX_HTML = str(configParser.get('config', 'INDEX_HTML'))
        MAX_SEARCH_COUNT = int(configParser.get('config', 'MAX_SEARCH_COUNT'))
        
        
        """dbConfig"""        
        DB_NAME = str(configParser.get('dbConfig', 'DB_NAME'))
        DB_ART_COLLECTION = str(configParser.get('dbConfig', 'DB_ART_COLLECTION'))
        MONGODB_URL = str(configParser.get('dbConfig', 'MONGODB_URL'))
        
        """crawlConfig"""
        CRAWL_WEBSITE = str(configParser.get('crawlConfig', 'CRAWL_WEBSITE'))
        
        
except Exception as e:
    print(e)
    exit()