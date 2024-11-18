import logging
logFile = "./logfile.log"
logLevel = logging.INFO
logging.basicConfig(level=logLevel, filename=logFile, filemode="a", format="%(asctime)-15s %(levelname)-8s %(message)s")

logger = logging.getLogger("logger")
import functools

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


