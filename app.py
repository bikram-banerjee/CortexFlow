from src.cortexflow.logger import logging
from src.cortexflow.exception import CustomException
import sys


if __name__ == "__main__":
    logging.info("Starting the application...")
    # Your application code goes here
    logging.info("Application finished.")

    try:
        # Simulating an error for demonstration
        result = 10 / 0
    except Exception as e:
        logging.info("Custom exception occurred: {}".format(str(e)))
        raise CustomException(str(e), sys.exc_info())