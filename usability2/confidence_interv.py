import random as rand
import numpy as np

rangel = int(input("size of max value (greater than 100): "))
if rangel < 100:
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

    k = 30
    bootstrapped_data = bootstrap(data, k)
    print(bootstrapped_data)
    tests = int(input("number of tests: "))
    actual_mean = (sum(bootstrapped_data) / len(bootstrapped_data))
    print(actual_mean)
    a=0
    while a < tests:
        print(bootstrapped_data[rand.randint(0, len(bootstrapped_data)-5):5])
        a+=1