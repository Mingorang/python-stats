import math
from math import factorial
import sys

#similar to the binomial distribution, will write code for poisson, geometric and negative binomial
#Should condense all probability distributions into this one
#Normal: mean(μ) and standard deviation(σ)
#Binomial: number of trials(n), probability of success(p)
#Poisson: events happen once at a time, randomly and independent of each other and happen at a constant rate; only 1 parameter λ (lambda)
#Geometric: number of trials(x)  until success with a probability(p) of success.
#Negative binomial: NB(r,p) --> trials up until the rth success, with a set probability (p)

#Set up choices for distributions 
print("Binomial")
print("Normal ")
print("Poisson ")
print("Geometric ")
print("Negative binomial")
choice = int(input("Choose a dist: "))
pdfcdf = bool(input("CDF or PDF (y/n)"))
 if choice == 1:
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
elif choice == 2:
    σ = float(input("Choose a value for standard deviation: "))
    μ = float(input("Choose a value for mean: "))     
    x = float(input("no. of successes / occurences: "))
    cdf_norm = 0
    if pdfcdf == 'y'
    a = float(input("Lower limits"))
    step = abs(x-a)/1000
    while a <= x:
    pdf_norm = ((1/(σ*math.sqrt(2*math.pi))))*((math.e)**(-0.5*((x-μ)/σ)**2))
    cdf_norm += pdf_norm
    print(f"Occurences (x): {x} | PDF: {pdf_norm:.20f} | Running CDF: {cdf_norm:.20f}")
    a+= step
