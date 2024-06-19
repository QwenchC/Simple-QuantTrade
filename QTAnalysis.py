# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import talib
import yfinance as yf
import matplotlib.pyplot as plt
import os
from trading_functions import download_data, load_data, compute_indicators, trading_strategy, plot_signals

def main():
    ticker = input("Enter the ticker symbol of the stock you want to analyze: ").upper()
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    
    # 下载数据并保存到文件
    download_data(ticker, start_date, end_date)
    
    # 从文件加载数据
    data = load_data(ticker)
    
    # 计算技术指标
    data = compute_indicators(data)
    
    # 应用交易策略
    data = trading_strategy(data)
    
    # 检查是否有买入或卖出信号
    if data['Buy_Signal'].isna().all() and data['Sell_Signal'].isna().all():
        print("No buy or sell signals were generated.")
    else:
        print("Buy and sell signals have been generated.")
    
    # 绘制价格和交易信号图
    plot_signals(data, ticker)

if __name__ == "__main__":
    main()
