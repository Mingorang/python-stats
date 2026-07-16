import math
import matplotlib.pyplot as plt
from math import factorial
import numpy as np
import sys
#binomial distribution an m sided dice with a (1/m) probability of landing on the mth side, all repeated n times

n = int(input("Number of trials: "))
p = float(input("Probability of success (0-1): "))
x = int(input("How many successes happened: "))

if x>n or (p>1 or p<0) :
    sys.exit()

bino_cdf=0
k=0
while k <= x:
    bino_pdf = (factorial(n) / (factorial(k) * factorial(n - k))) * (p**k) * ((1 - p)**(n - k))
    bino_cdf += bino_pdf
    print(f"Successes (k): {k} | PDF: {bino_pdf:.8f} | Running CDF: {bino_cdf:.8f}")
    k += 1
print(f"\nFinal Cumulative Distribution Function (CDF): {bino_cdf:.8f}")