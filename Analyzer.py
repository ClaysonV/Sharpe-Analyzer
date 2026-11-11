import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

def get_sharpe_ratios(tickers, risk_free_ticker, start_date, end_date):
    """
    Calculates the annualized Sharpe Ratios for a portfolio of assets.

    Args:
        tickers (list): Asset ticker symbols (e.g., ['AAPL', 'MSFT']).
        risk_free_ticker (str): Ticker for the risk-free rate proxy (e.g., '^IRX').
        start_date (str): Start date for historical data ('YYYY-MM-DD').
        end_date (str): End date for historical data ('YYYY-MM-DD').

    Returns:
        pandas.Series: Annualized Sharpe Ratios indexed by ticker, or None on failure.
    """
    tickers_with_rf = tickers + [risk_free_ticker]
    
    try:
        # Note: yfinance defaults to auto_adjust=True, so 'Close' is the adjusted close.
        data = yf.download(tickers_with_rf, start=start_date, end=end_date)['Close']
        if data.empty:
            print("Error: No data downloaded. Verify tickers and date range.")
            return None
    except Exception as e:
        print(f"Error downloading data: {e}")
        return None

    returns = data.pct_change().dropna()
    stock_returns = returns[tickers]
    
    # Normalize annualized T-bill yield to a daily rate
    rf_daily = returns[risk_free_ticker] / 100 / 252
    
    excess_returns = stock_returns.subtract(rf_daily, axis=0)
    
    daily_sharpe_ratio = excess_returns.mean() / excess_returns.std()
    
    # Annualize using 252 trading days
    annualized_sharpe_ratio = daily_sharpe_ratio * np.sqrt(252)

    return annualized_sharpe_ratio

def plot_sharpe_comparison(sharpe_ratios):
    """
    Generates a bar chart to compare the calculated Sharpe Ratios.

    Args:
        sharpe_ratios (pandas.Series): The annualized Sharpe Ratios from get_sharpe_ratios().
    """
    if sharpe_ratios is None or sharpe_ratios.empty:
        print("Plotting skipped: No Sharpe Ratios to display.")
        return

    colors = ['g' if x > 0 else 'r' for x in sharpe_ratios]
    
    plt.figure(figsize=(10, 6))
    

    sharpe_ratios.plot(kind='bar', color=colors, rot=0)
    
    plt.title('Annualized Sharpe Ratio Comparison', fontsize=16, fontweight='bold')
    plt.xlabel('Asset Tickers', fontsize=12)
    plt.ylabel('Annualized Sharpe Ratio (Risk-Adjusted Return)', fontsize=12)
    
    plt.axhline(0, color='grey', linestyle='--')
    
    plt.grid(axis='y', linestyle=':', alpha=0.7)
    
    for i, val in enumerate(sharpe_ratios):
        y_pos = val + (0.05 * np.sign(val))
        va_align = 'bottom' if val > 0 else 'top'
        plt.text(i, y_pos, f'{val:.2f}', ha='center', va=va_align)

    plt.tight_layout()
    
    print("\nDisplaying visual comparison chart...")
    plt.show()


if __name__ == "__main__":
    
    # 1. Asset Tickers: Define the assets to include in the analysis.
    stock_tickers = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'NVDA', 'JPM']
    
    # 2. Risk-Free Rate Proxy: Ticker for the benchmark risk-free asset.
    # ^IRX (13-Week T-Bill) is a common proxy for the US risk-free rate.
    risk_free_rate_ticker = '^IRX'
    start_date = '2020-01-01'
    end_date = '2026-11-1' 
    

    print(f"Sharpe Ratio analysis for: {', '.join(stock_tickers)}")
    print(f"Data Period: {start_date} to {end_date}\n")

    
    sharpe_ratios = get_sharpe_ratios(stock_tickers, risk_free_rate_ticker, start_date, end_date)

    if sharpe_ratios is not None:
    
        sorted_ratios = sharpe_ratios.sort_values(ascending=False)
        
        print("--- Analysis Results (Annualized Sharpe Ratio) ---")
        print(sorted_ratios)
        
        plot_sharpe_comparison(sorted_ratios)