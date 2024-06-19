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
    
    # �������ݲ����浽�ļ�
    download_data(ticker, start_date, end_date)
    
    # ���ļ���������
    data = load_data(ticker)
    
    # ���㼼��ָ��
    data = compute_indicators(data)
    
    # Ӧ�ý��ײ���
    data = trading_strategy(data)
    
    # ����Ƿ�������������ź�
    if data['Buy_Signal'].isna().all() and data['Sell_Signal'].isna().all():
        print("No buy or sell signals were generated.")
    else:
        print("Buy and sell signals have been generated.")
    
    # ���Ƽ۸�ͽ����ź�ͼ
    plot_signals(data, ticker)

if __name__ == "__main__":
    main()
