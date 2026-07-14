import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import odeint
from scipy.integrate import solve_ivp

# In form dy/dx = f(x,y) --> derivative is a function involving x and y

def dydx(x,y):
    return 1
v0=0
x=np.linspace(-10, 10,1000)

sol_m1 = odeint(dydx, y0=v0, t=x, tfirst=True)
sol_m2 = solve_ivp(dydx, t_span=(-10,max(x)), y0=[v0], t_eval=x)
v_sol_m1 = sol_m1.T[0]
v_sol_m2 = sol_m2.y[0]

plt.plot(x,v_sol_m1, label="odeint solution")
plt.plot(x,v_sol_m2, '--', label="solve_ivp solution")
plt.legend()
plt.ylabel('$f(x)$')
plt.xlabel('$x$')
plt.show()
