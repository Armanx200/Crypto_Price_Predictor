import os
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# Directory containing the dataset
data_dir = "Dataset"
model_dir = "Models"

# Function to preprocess data
def preprocess_data(df):
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.dropna(subset=['Date'], inplace=True)
    df.set_index('Date', inplace=True)
    df = df[['Open', 'High', 'Low', 'Close', 'Volume', 'Marketcap']]
    df.fillna(method='ffill', inplace=True)
    df.replace(0, np.nan, inplace=True)  # Replace 0 values with NaN
    df.dropna(inplace=True)  # Drop rows with NaN values
    return df

# Load datasets
def load_datasets(data_dir):
    datasets = {}
    for filename in os.listdir(data_dir):
        if filename.endswith('.csv'):
            coin_name = filename.split('_')[1].split('.')[0]
            df = pd.read_csv(os.path.join(data_dir, filename))
            datasets[coin_name] = preprocess_data(df)
    return datasets

# Predict future prices
def predict_future_prices(model, df):
    X = df[['Open', 'High', 'Low', 'Close', 'Volume', 'Marketcap']]
    future_prices = model.predict(X)
    return future_prices

# Main function
def main(coin_name):
    model_filename = os.path.join(model_dir, f'{coin_name}_model.pkl')
    if not os.path.exists(model_filename):
        print(f'Model for {coin_name} not found!')
        return

    model = joblib.load(model_filename)
    datasets = load_datasets(data_dir)
    
    if coin_name not in datasets:
        print(f'Dataset for {coin_name} not found!')
        return
    
    df = datasets[coin_name]
    future_prices = predict_future_prices(model, df)
    
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, future_prices, label='Predicted Future Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'Predicted Future Prices for {coin_name}')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    coin_name = input("Enter the cryptocurrency name (e.g., Bitcoin, Ethereum): ")
    main(coin_name)
