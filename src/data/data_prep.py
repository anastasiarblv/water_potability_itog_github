import pandas as pd
import numpy as np
import os

#train_data = pd.read_csv("./data/raw/train.csv") # C:\Users\honor\Desktop\ml_pipeline_papka_na_C_PC\data\raw\train.csv
#test_data = pd.read_csv("./data/raw/test.csv")   # C:\Users\honor\Desktop\ml_pipeline_papka_na_C_PC\data\raw\test.csv
def load_data(filepath):
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        raise Exception(f"Error loading data from {filepath}: {e}")    

#train_processed_data = fill_missing_with_mean(train_data)
#test_processed_data = fill_missing_with_mean(test_data)
def fill_missing_with_mean(df):
    try:
        for column in df.columns:
            if df[column].isnull().any():
                mean_value = df[column].mean() # тут мы ранее сделали опечтку и на самом деле тут mean_value
                df[column].fillna(mean_value,inplace=True) # тут мы ранее сделали опечтку и на самом деле тут mean_value
        return df
    except Exception as e:
        raise Exception(f"Error Filling missing values : {e}")

#data_path = os.path.join("data","processed")
#os.makedirs(data_path)
#train_processed_data.to_csv(os.path.join(data_path,"train_processed.csv"), index = False)
#test_processed_data.to_csv(os.path.join(data_path,"test_processed.csv"), index = False)
def save_data(df, filepath):
    try:
        df.to_csv(filepath, index = False)
    except Exception as e:
        raise Exception(f"Error saving parameters to {filepath}: {e}")
    

##############
def main():
    raw_data_path = "./data/raw/"
    processed_data_path = "./data/processed"
    try:
        train_data = load_data(os.path.join(raw_data_path, "train.csv"))
        test_data = load_data(os.path.join(raw_data_path, "test.csv"))
        train_processed_data = fill_missing_with_mean(train_data)
        test_processed_data = fill_missing_with_mean(test_data)
        
        os.makedirs(processed_data_path)
        save_data(train_processed_data, os.path.join(processed_data_path, "train_processed.csv"))
        save_data(test_processed_data, os.path.join(processed_data_path, "test_processed.csv"))
    except Exception as e:
        raise Exception(f"An error occurred : {e}")
if __name__ == "__main__":
    main()