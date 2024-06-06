import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Directory containing the dataset
data_dir = "Dataset"
model_dir = "Models"

# Ensure the model directory exists
os.makedirs(model_dir, exist_ok=True)

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

# Train model for a single coin
def train_model(df, coin_name):
    df['Target'] = df['Close'].shift(-1)
    df.dropna(inplace=True)

    X = df[['Open', 'High', 'Low', 'Close', 'Volume', 'Marketcap']]
    y = df['Target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f'{coin_name} Model MSE: {mse}')

    joblib.dump(model, os.path.join(model_dir, f'{coin_name}_model.pkl'))

# Main function
def main():
    datasets = load_datasets(data_dir)
    for coin_name, df in datasets.items():
        train_model(df, coin_name)

if __name__ == "__main__":
    main()
