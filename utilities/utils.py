import logging


class Utils:
    @staticmethod
    def custom_logger(logging_level=logging.INFO):
        # Create or get the logger named 'automationLogger'
        logger = logging.getLogger("automationLogger")

        # Set the logging level (default is INFO)
        logger.setLevel(logging_level)

        # Only add handlers if none exist (to avoid adding multiple handlers)
        if not logger.handlers:
            # Create a file handler to write log messages to a file named 'automation.log'
            # Set mode 'w' to overwrite the file every time the program runs
            file_handler = logging.FileHandler("automation.log", mode='a')
            file_handler.setLevel(logging_level)

            # Create a log message format (timestamp, logger name, log level, and the message)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            # Set the formatter for the file handler
            file_handler.setFormatter(formatter)

            # Add the file handler to the logger to write logs to the file
            logger.addHandler(file_handler)

        # Return the configured logger
        return logger
