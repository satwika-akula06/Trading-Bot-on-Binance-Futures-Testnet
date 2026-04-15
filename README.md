# Binance Futures Trading Bot (Testnet)

## Overview

This project is a Python-based trading bot that interacts with Binance Futures Testnet. It allows users to place MARKET, LIMIT and STOP-LIMIT orders via a Command Line Interface (CLI) and a Streamlit-based web UI.

---

## Features

- Place MARKET, LIMIT and STOP-LIMIT orders
- Supports both BUY and SELL operations
- CLI-based interaction using argparse
- Streamlit-based UI for better user experience
- Input validation and error handling
- Logging of API requests, responses and errors
- Mock mode support for testing without API access

---

## Tech Stack

- Python 3.x
- python-binance
- Streamlit
- argparse
- logging
- python-dotenv

---

## Project Structure

```
trading_bot/
│
|__ assets
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── app.py
├── cli.py
├── requirements.txt
├── README.md
├── .env.example
├── trading_bot.log
├── ui.png
```

---

## Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/satwika-akula06/Trading-Bot-on-Binance-Futures-Testnet.git
cd trading_bot
```

### 2. Create Virtual Environment

```
python -m venv venv
```

#### Windows:

```
venv\Scripts\activate
```

#### Mac/Linux:

```
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install python-binance python-dotenv
pip install -r requirements.txt
pip install streamlit
```

---

### 4. Configure Environment Variables

Create a `.env` file using `.env.example`:

```
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
USE_MOCK=True
```

---

## Usage

### CLI Usage

#### MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

#### LIMIT Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 70000
```

#### STOP-LIMIT Order

```
python cli.py --symbol BTCUSDT --side SELL --type STOP_LIMIT --quantity 0.01 --price 58000 --stop_price 59000
```

---

### Streamlit UI

Run the application:

```
streamlit run app.py
```

---

## Logging

Logs are stored in:

```
trading_bot.log
```

Logs include:

- Order request details
- Order responses
- Error messages

---

## ⚠️ Note

Due to Binance Testnet access limitations (KYC/region restrictions), a mock trading mode is implemented.

To use real Binance Testnet:

- Set `USE_MOCK=False`
- Provide valid API credentials

---

## Bonus Implementations

- STOP-LIMIT order support
- Streamlit UI dashboard

---

## UI Preview

```
![output look](ui1.png)
![output look](ui2.png)
```

---

## Author

Akula Satwika
