import pandas as pd
import numpy as np
import yfinance as yf

# download historical data for a currency pair
df = yf.download("EURUSD=X", start="2021-01-01", end="2022-04-14")

# calculate moving averages
ma50 = df['Close'].rolling(window=50).mean()
ma200 = df['Close'].rolling(window=200).mean()

# create a trading signal based on the moving averages
df['Signal'] = np.where(ma50 > ma200, 1, -1)

# calculate the returns of the strategy
df['Returns'] = df['Close'].pct_change() * df['Signal'].shift(1)

# calculate the cumulative returns of the strategy
df['Cumulative Returns'] = (1 + df['Returns']).cumprod()

# plot the cumulative returns of the strategy
df['Cumulative Returns'].plot()


print(df)
