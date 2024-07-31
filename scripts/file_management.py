import os
from pathlib import Path

def create_directory(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def move_file(src, dest):
    os.rename(src, dest)

if __name__ == "__main__":
    create_directory('data/processed_data')
    move_file('data/raw_data/utm_data.csv', 'data/processed_data/utm_data.csv')
