import inspect
import logging

class logBase:
    def logsetup(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler('./Utils/Reports/log.txt')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger





