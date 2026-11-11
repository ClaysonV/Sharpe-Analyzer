# Portfolio Sharpe Ratio Analyzer

A Python tool that calculates, compares, and visualizes the annualized Sharpe Ratios for a custom portfolio of assets using historical market data from Yahoo Finance.

## Features
* **Automated Data Retrieval:** Fetches historical closing prices for specified stock tickers and a risk-free rate proxy.
* **Risk-Adjusted Return Calculation:** Computes daily percentage returns, isolates excess returns, and calculates the annualized Sharpe Ratio for each asset.
* **Data Visualization:** Generates a bar chart comparing the Sharpe Ratios across the portfolio.

## Prerequisites
This project requires Python 3.x and the following libraries:
* `pandas`
* `yfinance`
* `numpy`
* `matplotlib`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ClaysonV/Sharpe-Analyzer.git
   cd Sharpe-Analyzer
   ```

2. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script from your terminal:
```bash
python analyzer.py
```
By default, the script analyzes the following tickers: AAPL, MSFT, GOOGL, TSLA, NVDA, and JPM against the 13-Week T-Bill (^IRX) from January 1, 2020, to November 1, 2026.

To analyze a different portfolio or date range, simply edit the stock_tickers, risk_free_rate_ticker, start_date, and end_date variables at the bottom of analyzer.py
