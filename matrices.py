import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


a = int(input("\n Choose a 2 or 3 dimensional transformation (2 or 3): "))

if a == 3:
    Ax = np.array([[[1],[0],[0]]])
    Ay = np.array([[[0],[1],[0]]])
    Az = None
elif a == 2:
    Ax = np.array([[[1],[0]]])
    Ay = np.array([[0],[1]])
    Az = np.array([[0],[0]])
else:
    print("Error in creating values")


rng = np.random.default_rng()
alpha = rng.integers(100, size=(a,a), endpoint=True)
#print("Alpha is: ", alpha)
print("\n X transformation is: \n", np.matmul(alpha, Ax))
print("\n Y transformation is: \n", np.matmul(alpha, Ay))
if a==3:
    print("\n Z transformation is: \n", np.matmul(alpha, Az))
elif a==2:
    print("There is no Z-plane transformation as the third dimension plane cannot be changed by a 2 dimensional matrix.")


#Maybe use to solve large systems of simultaneous equations?
