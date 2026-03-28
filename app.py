import sys
from src.cortexflow.logger import logging
from src.cortexflow.exception import CustomException
from src.cortexflow.components.data_ingestion import DataIngestion
from src.cortexflow.components.data_ingestion import DataIngestionConfig


if __name__ == "__main__":
    logging.info("Starting the application...")
    # Your application code goes here
    logging.info("Application finished.")

    try:
        #data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom exception occurred: {}".format(str(e)))
        raise CustomException(str(e), sys.exc_info())
    
