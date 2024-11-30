import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import yfinance as yf

# ターゲットを指定
ticker = "AMZN"

# データを収集
data = yf.download(ticker, start= "2003-01-01",end="2024-11-29", interval = "1d")
df = data

# 追加
df["Date"] = df.index
df = df.reset_index(drop=True)
df = df.drop("Volume", axis=1)
df_tmp = df.drop("Date", axis=1)

# 可視化する
df_tmp.plot()
plt.show()  # グラフ表示
df.info()
