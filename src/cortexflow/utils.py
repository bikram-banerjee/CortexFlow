import os
import sys
import pandas as pd
import pyodbc
from src.cortexflow.exception import CustomException
from src.cortexflow.logger import logging
from dotenv import load_dotenv

load_dotenv()

server = os.getenv('server')   # e.g. "DESKTOP-XXXX\\SQLEXPRESS"
database = os.getenv('db')

def read_sql_data():
    logging.info("Reading SQL Server database started")
    try:
        # Connection string for SQL Server (Windows Authentication)
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"Trusted_Connection=yes;"
        )

        logging.info("Connection to SQL Server successful")

        query = "SELECT * FROM Students"
        df = pd.read_sql(query, conn)

        print(df.head())

        return df

    except Exception as e:
        raise CustomException(str(e), sys.exc_info())