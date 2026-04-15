# Trading Bot (Binance Futures Testnet)

## Setup

pip install -r requirements.txt

## Run

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 30000

## Features

- Market & Limit order support
- CLI input
- Logging and error handling
- Modular structure