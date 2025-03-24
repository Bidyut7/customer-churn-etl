import pandas as pd
import os

def load_data_from_csv(file_path = './data/raw/E Commerce Dataset.xlsx'):
    try:
        df = pd.read_excel(file_path, sheet_name=1)
        print(f'data successfully loaded from {file_path}')
        print(f'data shape: {df.shape}')
        return df
    except Exception as e:
        print(f'Error loading data {e}')
        return None

if __name__ == '__main__':
    FILE_PATH = './data/raw/E Commerce Dataset.xlsx'
    df = load_data_from_csv(FILE_PATH)
    if df is not None:
        print(df.head())