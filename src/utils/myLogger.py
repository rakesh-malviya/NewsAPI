"""Usage

import myLogger.chatLogger as logger
logger.info("Hello")
logger.debug("Hello")

"""

import logging
import datetime



class MyLogger(object):
  def __init__(self,logger_name,log_dir,logfile_name="_myLog.log",datewise=True,mode='a+',log_format = '%(asctime)s %(levelname)s %(message)s',log_level=logging.DEBUG):
    self.datewise = datewise
    self.datetime = datetime.date.today().strftime('%d%b%Y')
    self.logger_name = logger_name
    self.logfile_name = logfile_name
    self.log_dir = log_dir
    self.mode=mode
    self.log_format = log_format
    if datewise:
      log_file_path = self.log_dir+"/"+self.datetime+self.logfile_name      
    else:      
      log_file_path = self.log_dir+"/"+self.logfile_name
      
    print 'log_file_path:',log_file_path    
    
    self.logger = logging.getLogger(self.logger_name)
    self.logger.handlers = []
    formatter = logging.Formatter(self.log_format)
    fileHandler = logging.FileHandler(log_file_path, mode=self.mode)
    fileHandler.setFormatter(formatter)
    
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    
    self.logger.setLevel(log_level)
    self.logger.addHandler(fileHandler)
    self.logger.addHandler(streamHandler)
    
  def info(self,msg):
    """Logs a message with level INFO on this logger. The arguments are interpreted as for debug()."""
    self.updateDate()
    self.logger = logging.getLogger(self.logger_name)
    self.logger.info(msg)
    
  def warning(self,msg):
    """Logs a message with level WARNING on this logger. The arguments are interpreted as for debug()."""
    self.updateDate()
    self.logger = logging.getLogger(self.logger_name)
    self.logger.warning(msg)
    
    
  def debug(self,msg):
    """Logs a message with level DEBUG on this logger. The msg is the message format string, and the args are the arguments which are merged into msg using the string formatting operator. (Note that this means that you can use keywords in the format string, together with a single dictionary argument.)"""
    self.updateDate()
    self.logger = logging.getLogger(self.logger_name)
    self.logger.debug(msg)
    
  def error(self,msg):
    """Logs a message with level ERROR on this logger. The arguments are interpreted as for debug()."""
    self.updateDate()
    self.logger = logging.getLogger(self.logger_name)
    self.logger.error(msg)
    
  def critical(self,msg):
    """Logs a message with level CRITICAL on this logger. The arguments are interpreted as for debug()."""
    self.updateDate()
    self.logger = logging.getLogger(self.logger_name)
    self.logger.critical(msg)    
      
  def updateDate(self):
    cur_datetime = datetime.date.today().strftime('%d%b%Y')
    if self.datewise and self.datetime!=cur_datetime:
      self.datetime = cur_datetime
      log_file_path = self.log_dir+"/"+self.datetime+self.logfile_name
      
      formatter = logging.Formatter(self.log_format)
      fileHandler = logging.FileHandler(log_file_path, mode=self.mode)
      fileHandler.setFormatter(formatter)
      self.logger.addHandler(fileHandler)
  


"""continuous Logger"""   
newsLogger = MyLogger(logger_name='myLogger',log_dir="logs/newsLogs",logfile_name="_myLog.log",datewise=True,mode='a+',log_format = '%(asctime)s %(levelname)s %(message)s')
dbLogger = MyLogger(logger_name='myLogger',log_dir="logs/dbLogs",logfile_name="_myLog.log",datewise=True,mode='a+',log_format = '%(asctime)s %(levelname)s %(message)s')



