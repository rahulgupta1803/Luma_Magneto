import inspect
import logging


class LogGenerator():
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("D:\\credence\\Luma_Magneto_Pytest_Project\\Log\\luma.log")
        log_format = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(funcName)s: %(lineno)d: %(message)s")
        logfile.setFormatter(log_format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger
