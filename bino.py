#imports
import math
import matplotlib.pyplot as plt
from math import factorial
import sys

#User inputs to find some binomial distribution
n = int(input("Number of trials: "))
p = float(input("Probability of success (0-1): "))
x = int(input("How many successes happened: "))
bino_cdf=0
k=0
#PDF is the probability of success at one point, CDF is the total successes from 0 to some point x.

#Logic part to check whether the distribution function is actually posiible with user input
if x>n or (p>1 or p<0) :
    sys.exit("Invalid: successes cannot be greater than the number of trials and probability of successes must be in the range 0 to 1.")
#Looping to find the total and the initial PDF from user input, binomial is discrete so goes up by 1    
while k <= x:
    bino_pdf = (factorial(n) / (factorial(k) * factorial(n - k))) * (p**k) * ((1 - p)**(n - k))
    bino_cdf += bino_pdf
    print(f"Successes (k): {k} | PDF: {bino_pdf:.20f} | Running CDF: {bino_cdf:.20f}")
    k += 1
print(f"\nFinal Cumulative Distribution Function (CDF): {bino_cdf:.16f}")
print(f"\nFinal Probability Density Function (PDF): {(factorial(n) / (factorial(x) * factorial(n - x))) * (p**x) * ((1 - p)**(n - x)):.16f}")
