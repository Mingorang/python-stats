import random as rand
import time
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import mplfinance as mpf
import os

#Very cool, should learn R for data analysis to do something with this data
    #Either build an AI bot that has access to the .csv file for the precise numerical data of OHLC
        #and the .png for visual needs such as ratio of bullish/bearish candles in a timeframe and other measures to make an index of market conditions.
    #

# Simulate OHLC stock data for a candle chart like the example image.
master_dir = os.path.dirname(os.path.abspath(__file__))
folder_name = os.path.join(master_dir, "processor")
os.makedirs(folder_name, exist_ok=True)
filename = os.path.join(folder_name, "generated_data.csv")
chart_file = os.path.join(folder_name, "stock_chart.png")

rand.seed(rand.randint(-1000000,1000000))
start_day = pd.Timestamp("2026-09-14")
all_timestamps = []
for offset in range(5):
    day = start_day + pd.Timedelta(days=offset)
    for hour in range(9, 18):
        all_timestamps.append(pd.Timestamp(day.date()) + pd.Timedelta(hours=hour))

rows = []
prev_close = 100.0
for idx, ts in enumerate(all_timestamps):
    open_price = prev_close
    close_price = open_price + rand.uniform(-6, 6)
    high = max(open_price, close_price) + rand.uniform(1.5, 4.5)
    low = min(open_price, close_price) - rand.uniform(1.5, 4.5)
    if low < 80:
        low = 80
    if high > 130:
        high = 130

    row = {
        "Open": round(open_price, 2),
        "High": round(high, 2),
        "Low": round(low, 2),
        "Close": round(close_price, 2),
    }
    rows.append((ts, row))
    prev_close = close_price

    print(f"{ts}: O={row['Open']} H={row['High']} L={row['Low']} C={row['Close']}")

daily = pd.DataFrame(
    [row for _, row in rows],
    index=pd.DatetimeIndex([ts for ts, _ in rows], name="Date")
)

daily.to_csv(filename)

print("\nCandlestick table:")
print(daily.head(12).to_string())

mpf.plot(
    daily,
    type="candle",
    style="charles",
    volume=False,
    figsize=(12, 6),
    ylabel="Price",
    title="Stock Price (9am-5pm, 5 Days)",
    savefig=chart_file,
)

print(f"\nSaved chart to: {chart_file}")