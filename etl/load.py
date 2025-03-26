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

def connect_db()
    try:
        engine = 