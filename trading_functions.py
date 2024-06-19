# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import talib
import yfinance as yf
import os
import matplotlib.pyplot as plt

# 下载股票数据并保存到文件
def download_data(ticker, start, end, data_folder='data'):
    data = yf.download(ticker, start=start, end=end)
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    data.to_csv(f'{data_folder}/{ticker}.csv')
    return data

# 从文件读取股票数据
def load_data(ticker, data_folder='data'):
    file_path = f'{data_folder}/{ticker}.csv'
    if os.path.exists(file_path):
        data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    else:
        raise FileNotFoundError(f"No data found for {ticker}. Please download the data first.")
    return data

# 计算技术指标
def compute_indicators(data):
    # MACD
    data['MACD'], data['MACD_Signal'], data['MACD_Hist'] = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    
    # KDJ
    data['K'], data['D'] = talib.STOCH(data['High'], data['Low'], data['Close'], fastk_period=9, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    data['J'] = 3 * data['K'] - 2 * data['D']
    
    # 均线 (MA)
    data['MA20'] = talib.SMA(data['Close'], timeperiod=20)
    data['MA50'] = talib.SMA(data['Close'], timeperiod=50)
    
    # BOLL线
    data['Upper'], data['Middle'], data['Lower'] = talib.BBANDS(data['Close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    
    # 去除缺失值
    data.dropna(inplace=True)
    
    return data

# 交易策略
def trading_strategy(data):
    buy_signals = []
    sell_signals = []
    position = 0  # 0: no position, 1: long, -1: short
    
    for i in range(len(data)):
        if position == 0:
            if data['Close'].iloc[i] > data['MA20'].iloc[i] and data['MACD'].iloc[i] > data['MACD_Signal'].iloc[i]:
                buy_signals.append(data['Close'].iloc[i])
                sell_signals.append(np.nan)
                position = 1
                print(f"Buy signal at {data.index[i]}: {data['Close'].iloc[i]}")
            elif data['Close'].iloc[i] < data['MA20'].iloc[i] and data['MACD'].iloc[i] < data['MACD_Signal'].iloc[i]:
                sell_signals.append(data['Close'].iloc[i])
                buy_signals.append(np.nan)
                position = -1
                print(f"Sell signal at {data.index[i]}: {data['Close'].iloc[i]}")
            else:
                buy_signals.append(np.nan)
                sell_signals.append(np.nan)
        elif position == 1:
            if data['Close'].iloc[i] < data['MA50'].iloc[i] or data['MACD'].iloc[i] < data['MACD_Signal'].iloc[i]:
                sell_signals.append(data['Close'].iloc[i])
                buy_signals.append(np.nan)
                position = 0
                print(f"Close long position at {data.index[i]}: {data['Close'].iloc[i]}")
            else:
                buy_signals.append(np.nan)
                sell_signals.append(np.nan)
        elif position == -1:
            if data['Close'].iloc[i] > data['MA50'].iloc[i] or data['MACD'].iloc[i] > data['MACD_Signal'].iloc[i]:
                buy_signals.append(data['Close'].iloc[i])
                sell_signals.append(np.nan)
                position = 0
                print(f"Close short position at {data.index[i]}: {data['Close'].iloc[i]}")
            else:
                buy_signals.append(np.nan)
                sell_signals.append(np.nan)
    
    data['Buy_Signal'] = buy_signals
    data['Sell_Signal'] = sell_signals
    return data

# 绘制价格和交易信号图
def plot_signals(data, ticker):
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price')
    plt.plot(data['MA20'], label='MA20')
    plt.plot(data['MA50'], label='MA50')
    plt.plot(data['Upper'], label='Upper Band')
    plt.plot(data['Middle'], label='Middle Band')
    plt.plot(data['Lower'], label='Lower Band')
    
    # 直接在图线上标注买入和卖出信号
    plt.scatter(data.index, data['Buy_Signal'], label='Buy Signal', marker='^', color='green')
    plt.scatter(data.index, data['Sell_Signal'], label='Sell Signal', marker='v', color='red')
    
    plt.title(f'{ticker} Price and Trading Signals')
    plt.legend()
    plt.show()
