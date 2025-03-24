import pandas as pd
import os
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from extract import load_data_from_csv

def clean_data(df):
    df.dropna(inplace=True)
    return df

def encode_categorical(df):
    df = pd.get_dummies(df, drop_first=True)
    return df

def normalise_data(df):
    scaler = StandardScaler()
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[num_cols] = scaler.fit_transform(df[num_cols])
    return df

def save_clean_data(df, file_path="./data/processed/customers_cleaned.csv"):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)
    print(f'cleaned data saved to {file_path}')

if __name__=='__main__':
    df = load_data_from_csv(file_path = './data/raw/E Commerce Dataset.xlsx')
    if df is not None:
        df = clean_data(df)
        df = encode_categorical(df)
        df = normalise_data(df)
        save_clean_data(df)
        print('Data Transformation completed')