import ConfigParser
import os
import json
configFileLoc = "config/newsAPI.cfg"

SERVERIP = None
API_PORT = None
DB_NAME  = None
DB_ART_COLLECTION = None

try:
    if not os.path.exists(configFileLoc):
        print "No configuration file found. " + '\n'
        raise Exception('Config File not found')
    else:
        configParser = ConfigParser.RawConfigParser()
        configParser.read(configFileLoc)
        API_PORT = int(configParser.get('config', 'API_PORT'))
        SERVERIP = str(configParser.get('config', 'SERVERIP'))
        
        
        """dbconfig"""        
        DB_NAME = str(configParser.get('dbconfig', 'DB_NAME'))
        DB_ART_COLLECTION = str(configParser.get('dbconfig', 'DB_ART_COLLECTION'))     
        
except Exception as e:
    print(e)
    exit()