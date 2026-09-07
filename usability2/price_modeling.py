import random as rand
import time
import pandas as pd
import mplfinance as mpf
import matplotlib

#From a youtube video, assume price of a stock is n, n can range from 85 to 115, we then use another randomised factor to simulate price movement of a stock over time

for i in range(50):
    n = 100+(rand.randint(-15,15))
    print(n)
    n+=1
    time.sleep(1/50)
