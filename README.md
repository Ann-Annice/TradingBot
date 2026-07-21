# Binance Futures Demo Trading Bot

A Python-based command-line trading bot that connects to the Binance Futures Demo (Testnet) API and allows users to place Market and Limit orders with input validation and logging.

---

## Features

- Connects to Binance Futures Demo (Testnet)
- Place Market Orders
- Place Limit Orders
- Input validation
- Command Line Interface (CLI)
- Logging of all trading activity
- Environment variable support using `.env`

---

## Project Structure

```
TradingBot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── cli.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│   └── trading_bot.log
│
├── .env
├── main.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python 3
- python-binance
- python-dotenv
- argparse
- logging

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd TradingBot
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
API_KEY=YOUR_BINANCE_API_KEY
API_SECRET=YOUR_BINANCE_API_SECRET
```

Use Binance Futures Demo (Testnet) API credentials.

---

## Run the Project

### Market Order

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

Example Output

```
Symbol : BTCUSDT
Side : BUY
Type : MARKET
Quantity : 0.001

Order placed successfully!
```

---

### Limit Order

```bash
python main.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 60000
```

Example Output

```
Symbol : BTCUSDT
Side : BUY
Type : LIMIT
Quantity : 0.001
Price : 60000

Order placed successfully!
```

---

## Input Validation

The application validates:

- Trading Symbol
- Order Side (BUY / SELL)
- Order Type (MARKET / LIMIT)
- Quantity
- Limit Price

Invalid input generates clear error messages.

---

## Logging

Every order request and response is automatically saved to:

```
logs/trading_bot.log
```

Example:

```
INFO | MARKET Order -> BUY 0.001 BTCUSDT
INFO | LIMIT Order -> BUY 0.001 BTCUSDT @ 60000
```

---

## Requirements

```
python-binance
python-dotenv
```

Install using:

```bash
pip install -r requirements.txt
```

---

## Future Improvements

- Stop Loss Orders
- Take Profit Orders
- Cancel Open Orders
- Order History
- Position Management
- Account Balance Display
- Risk Management
- Strategy Automation
- Unit Testing

---

## Author

**Ann Annice**

Full Stack Developer

Python • REST APIs • Binance API

---

## License

This project is developed for educational and learning purposes.