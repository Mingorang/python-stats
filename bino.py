import math
import matplotlib.pyplot as plt
from math import factorial
import numpy as np
#binomial distribution an m sided dice with a (1/m) probability of landing on the mth side, all repeated n times

n = int(input("Number of trials: "))
p = float(input("Probability of success (0-1): "))
x = int(input("How many success happened: "))

def bino_pdf(x)
    bino_pdf = (factorial(n) / ((factorial(x)*factorial(n-x)))) * (p**x) * ((1-p)**(n-x))

i=0
bino_cdf = 0
while i < (n+1):
    bino_cdf = bino_cdf + bino_pdf
    i+=1
print(bino_cdf)
