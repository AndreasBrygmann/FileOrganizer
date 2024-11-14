'''
import logging
logging.basicConfig(level=logging.INFO)
from fileHandling import writeLogg
'''
import logging
logFile = "./logfile.log"
logLevel = logging.INFO
logging.basicConfig(level=logLevel, filename=logFile, filemode="a", format="%(asctime)-15s %(levelname)-8s %(message)s")

logger = logging.getLogger("logger")
import functools
'''
from typing import Any, Callable

def logg(func):
    logger.info(func.__name__)
    logger.info(func)

# decorator
def logg(func):
    def wrapper(*args, **kwargs):
        try:
            logging.info("started '{0}', parameters : {1} and {2}".
                         format(func.__name__, args, kwargs))
            return func(*args, **kwargs)
        except Exception as e:
            logging.exception(e)
    #return wrapper
    writeLogg(wrapper)

def writeLogEntry(entry):
    writeLogEntry(entry)

def writeEntry():
    return

def logged (level , name =None , message = None ):
    def decorate ( func ):
        logname = name if name else func .  __module__
        log = logging . getLogger ( logname )
        logmsg = message if message else func . __name__
        #@wraps ( func )
        def wrapper (* args , ** kwargs ):
            log .log (level , logmsg )
            return func (* args , ** kwargs )
        return wrapper
    return decorate
'''
#def logg(func: callable[..., Any], logger: logging.Logger) -> callable[..., Any]:
def logg(func, logger: logging.Logger):
    functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        try:
            logging.info(f"{func.__name__} | {result}")
        except Exception as e:
            logging.exception(e)
        return result
    return wrapper

defaultLogger = functools.partial(logg, logger=logger)


