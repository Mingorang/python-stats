import math
from math import factorial
import sys
#similar to the binomial distribution, will write code for poisson, geometric and negative binomial
#Should condense all probability distributions into this one

#Binomial: number of trials(n), probability of success(p)
#Normal: mean(μ) and standard deviation(σ)
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
pdfcdf = bool(input("CDF or PDF (y/n): ").strip().lower().startswith('y'))
#Very large if statement for processing the distributions, adding plots will be in the future (maybe)


#Binomial - discrete
if choice == 1:
    discrete_check = True
    n = int(input("Number of trials: "))
    p = float(input("Probability of success (0-1): "))
    x = int(input("How many successes happened: "))
    bino_cdf=0
    k=0
    #PDF is the probability of success at one point, CDF is the total successes from 0 to some point x.

    #Logic part to check whether the distribution function is actually possible with user input
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
#Normal - continuous
elif choice == 2:
    discrete_check = False
    μ = float(input("Choose a value for mean: "))     
    σ = float(input("Choose a value for standard deviation: "))
    x = float(input("no. of successes / occurences: "))
    cdf_norm = 0
    if pdfcdf == True:
        a = float(input("Lower limit: "))
        steps = 1000
        if x == a:
            sys.exit("You should have chosen PDF then.")
        else:
            step = (x - a) / steps
        while (a <= x and step > 0) or (a >= x and step < 0):
            pdf_norm = (1 / (σ * math.sqrt(2 * math.pi))) * (math.e ** (-0.5 * ((a - μ) / σ) ** 2))
            cdf_norm += pdf_norm * abs(step)
            print(f" Occurences (a): {a:>12.4g} | PDF: {pdf_norm:>12.6g} | Running CDF: {cdf_norm:>12.6g}")
            a += step
            
    else:
            pdf_norm = (1 / (σ * math.sqrt(2 * math.pi))) * (math.e ** (-0.5 * ((x - μ) / σ) ** 2))
            print(f"A value of {x} in this distribution has a PDF of {pdf_norm:>18.15f}")
#Poisson - discrete
elif choice == 3:
    #Maybe use the gamma function for calculating factorials with decimals, but i should learn how to write functions soon
    λ = int(input("Value for poisson paramter: "))
    x = int(input("no. of successes / occurences: "))
    pois_cdf = 0
    k=0
    if pdfcdf == True:
        while k <= x:
            pois_pdf = ((math.e)**(-1*λ))*(λ**k)*(1/(factorial(k)))
            pois_cdf += pois_pdf
            print(f"Successes (k): {k:>4.2g} | PDF: {pois_pdf:>12.6g} | Running CDF: {pois_cdf:12.6g}")
            k += 1
        print(f"\nFinal Cumulative Distribution Function (CDF): {pois_cdf:16.15g}")
    else:
        pois_pdf = ((math.e)**(-1*λ))*(λ**x)*(1/(factorial(x)))
        print(f"X : {x} | PDF : {pois_pdf:10.9g}")


#Geometric
elif choice == 4:
    p = float(input("Choose a value for probability: "))
    x = float(input("no. of successes / occurences: "))  
    if (p<0) or (p>1):
        sys.exit("Error as probability cant be outside of 0 and 1.")
    else:
        pass
    geom_cdf = 0
    k = 1
    if pdfcdf == True:
        while k<= x:
            geom_pdf = p*(1-p)**(k-1)
            geom_cdf += geom_pdf
            print(f"Successes: ({k}) | PDF: {geom_pdf:>12.6g} | Running CDF: {geom_cdf:>12.6g}")
            k+=1
        print(f"Final CDF is:  {geom_cdf:>24.22g}")
    else:
            geom_pdf = p*(1-p)**(x-1)
            print(f"PDF at point {x} is {geom_pdf:>17.15g}")

#Negative Binomial
elif choice == 5:
    p = float(input("Choose a value for probability: "))
    r = int(input("Testing up until the rth success: "))
    x = int(input("no. of successes / occurences: "))  
    negbi_cdf = 0
    k = 1
    if pdfcdf == True:
        while k<= x:
            negbi_pdf =  (factorial(k-1)/(factorial(r-1)*factorial(k-r)))*(p**r)*(1-p)**(k-r)
            negbi_cdf += negbi_pdf
            print(f"Successes: ({k}) | PDF: {negbi_pdf:>12.6g} | Running CDF: {negbi_cdf:>12.6g}")
            k+=1
        print(f"Final CDF is:  {negbi_cdf:>24.22g}")
    else:
            negbi_pdf =  (factorial(x-1)/(factorial(r-1)*factorial(x-r)))*(p**r)*(1-p)**(x-r)
            print(f"PDF at point {x} is {negbi_pdf:>17.15g}")


