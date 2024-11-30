import os
import datetime as dt
import pandas as pd
import yfinance as yf
import matplotlib as mp
stock_code="7203"
stock_code_dr=stock_code + ".T"
first='2023-09-01'
last = dt.date.today()
df = yf.download(stock_code_dr, start=first, end=last)
df.to_csv('stockdata_yahoo.csv') 

#Tikerで一つの銘柄の情報を取得　例はトヨタ 。2024/11/28時点
STOCK = yf.Ticker("7203.T") 

try:
    STOCK_info = STOCK.info
    print(f"データ取得成功: {STOCK_info['longName']}の情報を取得しました。")
except KeyError as e:
    print(f"キーエラー: {e}が見つかりません。")
except ConnectionError:
    print("ネットワークエラー: インターネット接続を確認してください。")
except Exception as e:
    print(f"データ取得エラー: {e}")

# 情報取得(.info)
STOCK_info = STOCK.info

# シンボル
print(f"{STOCK_info['underlyingSymbol']=}")

# 会社名
print(f"{STOCK_info['shortName']=}")

print(f"{STOCK_info['longName']=}")

# 現在値
print(f"{STOCK_info['currentPrice']=}円")

# 52週最高値
print(f"{STOCK_info['fiftyTwoWeekLow']=}円")

# 52週最低値
print(f"{STOCK_info['fiftyTwoWeekHigh']=}円")

#bs/pl/cf

#Tikerでトヨタを指定。
STOCK = yf.Ticker("7203.T") 
    
# 損益計算書P/L (.income_stmt/.quarterly_income_stmt)------------------------
STOCK_income_stmt = STOCK.income_stmt
print(f'{type(STOCK_income_stmt)=}\n{STOCK_income_stmt}')

# 四半期ごとの場合は
STOCK_quarterly_income_stmt = STOCK.quarterly_income_stmt
print(f'{type(STOCK_quarterly_income_stmt)=}\n{STOCK_quarterly_income_stmt}')

# csvへ出力
STOCK_income_stmt.to_csv(STOCK_info['underlyingSymbol']+"_損益計算書.csv")


# 貸借対照表B/S (.balance_sheet/.quarterly_balance_sheet)--------------------
STOCK_balance_sheet = STOCK.balance_sheet
print(f'{type(STOCK_balance_sheet)=}\n{STOCK_balance_sheet}')

# 四半期ごとの場合は
STOCK_quarterly_balance_sheet = STOCK.quarterly_balance_sheet
print(f'{type(STOCK_quarterly_balance_sheet)=}\n{STOCK_quarterly_balance_sheet}')

# csvへ出力
STOCK_balance_sheet.to_csv(STOCK_info['underlyingSymbol']+"_貸借対照表.csv")


# キャッシュフロー計算書C/F (.cashflow /.quarterly_cashflow )----------------
STOCK_cashflow = STOCK.cashflow
print(f'{type(STOCK_cashflow)=}\n{STOCK_cashflow}')

# 四半期ごとの場合は
STOCK_quarterly_cashflow = STOCK.quarterly_cashflow
print(f'{type(STOCK_quarterly_cashflow)=}\n{STOCK_quarterly_cashflow}')

# csvへ出力
STOCK_cashflow.to_csv(STOCK_info['underlyingSymbol']+"_キャッシュフロー計算書.csv")

