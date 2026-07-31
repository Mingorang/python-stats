import random as rand
import numpy as np
rangel = int(input("size of max value (greater than 100): "))
if rangel <= 100:
    raise ValueError("Bad range")
elif type(rangel) != int:
    raise ValueError("Bad input type")
def data_randomiser(n):
    # Generates n random numbers between 0 and rangel
    if rangel < 1:
        raise ValueError("Bad range")

    return [rand.randint(0, rangel) for _ in range(n)]

def bootstrap(data, n):
    # Draw n bootstrap samples with replacement from data
    if not data:
        raise ValueError("Data cannot be empty")

    return np.random.choice(data, size=n, replace=True).tolist()

if __name__ == "__main__":
    data = data_randomiser(10)
    print(data)

    population_size = int(3e7)
    bootstrapped_data = bootstrap(data, population_size)
    print(f"There were {len(bootstrapped_data)} bootstrapped samples generated!")
    tests = int(input("number of tests: "))
    actual_mean = (sum(bootstrapped_data) / len(bootstrapped_data))
    print(f"Actual mean: {actual_mean:<12.4f}")
    loop=0
    t_f = rand.randint(0,1)
    while loop < tests:
        x = rand.randint(30,len(bootstrapped_data)-30)
        if t_f == 0:
            bootstrapped_data[x:x+45]
            sample_mean = (sum(bootstrapped_data[x:x+45]) / 45)
            print(f"Sample mean: {sample_mean:<12.4f}") 
        elif t_f == 1:
            bootstrapped_data[x-45:x]
            sample_mean = (sum(bootstrapped_data[x-45:x]) / 45)
            print(f"Sample mean: {sample_mean:<12.4f}")
        loop+=1
#We use the sample_mean to plot points, a histogram showing 