import os,sys
import logging
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler
import threading
import configparser
import time

class LogSignleton(object):
    """
    CRITICAL = 50
    FATAL = CRITICAL
    ERROR = 40
    WARNING = 30
    WARN = WARNING
    INFO = 20
    DEBUG = 10
    NOTSET = 0
    """
    def __init__(self, log_config):
        pass

    def __new__(cls, log_config):
        mutex=threading.Lock()
        mutex.acquire() # 上锁，防止多线程下出问题
        if not hasattr(cls, 'instance'):
            cls.instance = super(LogSignleton, cls).__new__(cls)
            config = configparser.ConfigParser()
            config.read(log_config, encoding='utf-8')
            cls.instance.log_filename = config.get('LOGGING', 'log_file')
            cls.instance.max_bytes_each = int(config.get('LOGGING', 'max_bytes_each'))
            cls.instance.backup_count = int(config.get('LOGGING', 'backup_count'))
            cls.instance.fmt = config.get('LOGGING', 'fmt')
            cls.instance.log_level_in_console = int(config.get('LOGGING', 'log_level_in_console'))
            cls.instance.log_level_in_logfile = int(config.get('LOGGING', 'log_level_in_logfile'))
            cls.instance.logger_name = config.get('LOGGING', 'logger_name')
            cls.instance.console_log_on = int(config.get('LOGGING', 'console_log_on'))
            cls.instance.logfile_log_on = int(config.get('LOGGING', 'logfile_log_on'))
            cls.instance.logger = logging.getLogger(cls.instance.logger_name)
            cls.instance.__config_logger()
        mutex.release()
        return cls.instance

    def get_logger(self):
        return self.logger


    def create_file(self,filename):
        #path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_filename = path+filename
        if not os.path.isfile(log_filename):
            fd = open(log_filename, mode='w', encoding='utf-8')
            fd.close()
        else:
            pass
        return log_filename

    def __config_logger(self):
        # 设置日志格式
        fmt = self.fmt.replace('|','%')
        formatter = logging.Formatter(fmt)

        if self.console_log_on == 1: # 如果开启控制台日志
            console = logging.StreamHandler()
            console.setFormatter(formatter)
            self.logger.addHandler(console)
            self.logger.setLevel(self.log_level_in_console)

        if self.logfile_log_on == 1: # 如果开启文件日志

            log_filename = path+self.log_filename+'_'+time.strftime("%Y-%m-%d")+'.log'
            if not os.path.isfile(log_filename):
                fd = open(log_filename, mode='w', encoding='utf-8')
                fd.close()
            else:
                pass
            rt_file_handler = TimedRotatingFileHandler(log_filename, when='D', encoding='utf-8',interval=1,backupCount=self.backup_count)
            rt_file_handler.setFormatter(formatter)
            self.logger.addHandler(rt_file_handler)
            self.logger.setLevel(self.log_level_in_logfile)


path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
conf_log_path = path+'/config/config.ini'

logsignleton = LogSignleton(conf_log_path)

logger = logsignleton.get_logger()


