# Quantitative Trading Analysis Project

This project is designed to perform quantitative trading analysis on various stocks and indices using technical indicators. The project downloads historical data, computes technical indicators, applies a trading strategy, and plots buy/sell signals.

## Features

- Download historical stock data from Yahoo Finance.
- Compute technical indicators using TA-Lib.
- Apply a simple trading strategy based on technical indicators.
- Plot stock prices along with buy and sell signals.

## Requirements

- Python 3.7 or higher
- pandas
- numpy
- TA-Lib
- yfinance
- matplotlib

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/quantitative-trading-analysis.git
    cd quantitative-trading-analysis
    ```

2. Install the required packages:
    ```bash
    pip install pandas numpy ta-lib yfinance matplotlib
    ```

## Usage

1. Run the main script:
    ```bash
    python main.py
    ```

2. Enter the ticker symbol of the stock or index you want to analyze when prompted. For example:
    - Apple Inc.: `AAPL`
    - Shanghai Composite Index: `000001.SS`
    
3. Enter the start date and end date for the analysis period in the format `YYYY-MM-DD`.

## Project Structure

- `main.py`: The main script to run the analysis.
- `trading_functions.py`: Contains functions for downloading data, computing indicators, applying trading strategies, and plotting signals.
- `README.md`: Project documentation.

## Example

Here's an example of how to run the project:

```plaintext
Enter the ticker symbol of the stock you want to analyze (e.g., AAPL for Apple, 000001.SS for Shanghai Composite Index): AAPL
Enter the start date (YYYY-MM-DD): 2018-01-01
Enter the end date (YYYY-MM-DD): 2022-01-01
