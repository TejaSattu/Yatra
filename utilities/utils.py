import inspect
import logging


class Utils():

    def custom_logger(logging_level = logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging_level)
        file_handler = logging.FileHandler("Automation.log")
        # console_handler = logging.StreamHandler()
        formatter =logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # console_handler.setFormatter(formatter)
        # logger.addHandler(console_handler)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        #
        return logger
