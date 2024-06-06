# 🚀 Crypto Price Predictor 📈

Welcome to the **Crypto Price Predictor** repository! This project aims to forecast cryptocurrency prices using machine learning models. 🌟

![Bitcoin Prediction](https://github.com/Armanx200/Crypto_Price_Predictor/blob/main/Figure.png)

## 📂 Project Structure

- `Dataset/` 📊: Contains the historical cryptocurrency data in CSV format.
- `Models/` 🧠: Stores the trained machine learning models.
- `Crypto_Price_Model.py` 🤖: Script to train the models.
- `Crypto_Price_Predictor.py` 🔮: Script to predict future prices using the trained models.

## 🛠️ How to Use

### 1. Train the Model

First, run `Crypto_Price_Model.py` to train the models for all the cryptocurrencies. The trained models will be saved in the `Models` directory.

```bash
python Crypto_Price_Model.py
```

### 2. Predict Future Prices

Next, use `Crypto_Price_Predictor.py` to load a trained model and predict future prices for a specified cryptocurrency.

```bash
python Crypto_Price_Predictor.py
```

Enter the name of the cryptocurrency (e.g., Bitcoin, Ethereum) when prompted.

## 🏆 Model Performance

Here are the Mean Squared Error (MSE) values for our models:

- **Aave**: 2053.1783
- **BinanceCoin**: 64902.0719
- **Bitcoin**: 298114964.3461
- **Cardano**: 0.1006
- **ChainLink**: 121.0245
- **Cosmos**: 110.5456
- **CryptocomCoin**: 0.0006
- **Dogecoin**: 0.0188
- **EOS**: 0.3773
- **Ethereum**: 487633.3648
- **Iota**: 0.0150
- **Litecoin**: 189.7667
- **Monero**: 237.8501
- **NEM**: 0.0008
- **Polkadot**: 13.2997
- **Solana**: 152.0202
- **Stellar**: 0.0020
- **Tether**: 7.7837e-06
- **Tron**: 7.6098e-05
- **Uniswap**: 18.8259
- **USDCoin**: 8.8966e-06
- **WrappedBitcoin**: 40597001.4039
- **XRP**: 0.0072

## 🌟 Features

- Predicts future prices of various cryptocurrencies.
- Utilizes Random Forest Regressor for accurate predictions.
- Handles missing data and performs necessary preprocessing.

## 📦 Dependencies

Ensure you have the required libraries installed. You can install them using pip:

```bash
pip install pandas numpy scikit-learn joblib matplotlib
```

## 📫 Connect with Me

For any queries or discussions, feel free to reach out via my [GitHub profile](https://github.com/Armanx200).

---

Happy predicting! 🚀📈

---

```

### Instructions for Running the Scripts

1. **Train the Model:**
   - Run `Crypto_Price_Model.py` to train the models for all the cryptocurrencies and save them to the "Models" directory.

   ```bash
   python Crypto_Price_Model.py
   ```

2. **Predict Future Prices:**
   - Run `Crypto_Price_Predictor.py` to load a trained model from the "Models" directory and predict future prices for a specified cryptocurrency.

   ```bash
   python Crypto_Price_Predictor.py
   ```
   - Enter the name of the cryptocurrency (e.g., Bitcoin, Ethereum) when prompted.

### Dependencies
Make sure you have the required libraries installed. You can install them using pip:

```bash
pip install pandas numpy scikit-learn joblib matplotlib
```

These updated scripts will now save the trained models in the "Models" directory and load them from there for prediction.
