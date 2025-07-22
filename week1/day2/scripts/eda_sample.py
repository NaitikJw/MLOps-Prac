# eda_sample.py

import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    print("Shape:", df.shape)
    print("Head:\n", df.head())

# Example usage
if __name__ == "__main__":
    print("This is a placeholder EDA script. Replace 'data.csv' with your file path.")
