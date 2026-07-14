import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import odeint
from scipy.integrate import solve_ivp

# In form dy/dx = f(x,y) --> derivative is a function involving x and y
a = int(input("Lower limit of x: "))
b = int(input("Upper limit of x: "))
choice = input("Simple ODE or coupled ODE? (1/2)")
if choice == '1':
    def dydx(x,y):
        return 1
    v0=0
    x=np.linspace(a, b,1000)

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

elif choice == '2':
   
    def dS_dx(x, S):
        y1, y2 = S
        dy1_dx = y1 + y2 * np.sin(x) 
        dy2_dx = y1 * y2 - x
        
        return [dy1_dx, dy2_dx]

    S0 = [1.0, 0.5] # y1(0) = 1.0, y2(0) = 0.5
    x = np.linspace(0, 5, 100)

    solution_coupled = odeint(dS_dx, y0=S0, t=x, tfirst=True)

    y1_sol = solution_coupled.T[0] 
    y2_sol = solution_coupled.T[1]

    plt.plot(x, y1_sol, label="y1")
    plt.plot(x, y2_sol, label="y2")
    plt.legend()
    plt.title("Coupled First-Order ODEs")
    plt.show()
