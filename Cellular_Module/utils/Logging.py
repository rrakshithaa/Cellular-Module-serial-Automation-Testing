import logging
import os
import datetime


class Logger:
    _logger_instance = None
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_____%H-%M-%S')
    LOG_DIR = "logs"
    LOG_FILE = f"Cellular_{timestamp}.log"


    @staticmethod
    def get_logger():
        if Logger._logger_instance is None:
            # Ensure log directory exists
            if not os.path.exists(Logger.LOG_DIR):
                os.makedirs(Logger.LOG_DIR)

            logger = logging.getLogger("Logs")
            logger.setLevel(logging.DEBUG)

            # File handler for logging to file inside the logs directory
            log_file_path = os.path.join(Logger.LOG_DIR, Logger.LOG_FILE)
            file_handler = logging.FileHandler(log_file_path)
            console_handler = logging.StreamHandler()

            # Set logging levels
            file_handler.setLevel(logging.DEBUG)
            console_handler.setLevel(logging.DEBUG)  # Print all levels to the console

            # Log format
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add handlers to the logger
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

            Logger._logger_instance = logger

        return Logger._logger_instance


# Create logger instance
logger = Logger.get_logger()
