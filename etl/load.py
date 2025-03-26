import pandas as pd
import os
import psycopg2
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'customer_churn')
DB_USER = os.getenv('DB_USER', 'shreysharma')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'shrey123')
DB_PORT = os.getenv('DB_PORT', '5432')

def connect_db():
    try:
        engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        print('Connected to the database')
        return engine
    except Exception as e:
        print('Error connecting to the database', e)
        return None

def load_data_to_db(file_path = 'data/processed/customers_cleaned.csv', table_name='customer_churn'):
    try:
        df = pd.read_csv(file_path)
        engine = connect_db()
        if engine is not None:
            df.to_sql(table_name, engine, if_exists='replace', index=False)
            print('Data loadded successfully into the table')
    except Exception as e:
        print('Error loading the data into the table', e)

if __name__ == '__main__':
    load_data_to_db()