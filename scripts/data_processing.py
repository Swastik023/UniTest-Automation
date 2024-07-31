import pandas as pd
import numpy as np

def process_data(file_path, output_path):
    data = pd.read_csv(file_path)
    processed_data = data.apply(np.mean, axis=0)
    processed_data.to_csv(output_path, index=False)

if __name__ == "__main__":
    raw_data_path = 'data/raw_data/utm_data.csv'
    processed_data_path = 'data/processed_data/processed_utm_data.csv'
    process_data(raw_data_path, processed_data_path)
