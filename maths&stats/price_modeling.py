import random as rand
import time
import pandas as pd
import mplfinance as mpf
import matplotlib
import csv
import os

#From a youtube video, assume price of a stock is n, n can range from 85 to 115, we then use another randomised factor to simulate price movement of a stock over time

master_dir = os.path.dirname(os.path.abspath(__file__))
folder_name = os.path.join(master_dir, "my_data_folder")
os.makedirs(folder_name, exist_ok=True)
filename = os.path.join(folder_name, "generated_data.csv")
with open(filename, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    for i in range(50):
        n = 100 + rand.randint(-15, 15)
        print(n)
        writer.writerow([n])  # Writes immediately to file
        time.sleep(1 / 50)
daily = pd.read_csv('maths&stats/my_data_folder/generated_data.csv',index_col=0,parse_dates=True)
daily.index.name = "Date"
daily.shape
daily.head(3)
daily.tail(3)