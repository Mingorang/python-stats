import random as rand
import numpy as np
import sys
def data_randomiser(n):
    #Generates 'n' random numbers between 0 and 10000
    range = int(input("size of max value: "))
    if range < 1:
        sys.exit("Bad range")

    data = []
    for i in range(n):
        data.append(rand.randint(0, range))
    return data
print(data_randomiser(10))

k=3000

def bootsrap(data, n):
    sample_range = round(range/k)
    