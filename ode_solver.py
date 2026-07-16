import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import odeint
from scipy.integrate import solve_ivp

# In form dy/dx = f(x,y) --> derivative is a function involving x and y
a = int(input("Lower limit of x: "))
b = int(input("Upper limit of x: "))
choice = input("Simple ODE or coupled ODE? (1/2): ")

def lin_log_auto_scale(y_sol,threshold = 100):
    if choice == '1':
        def dydx(x,y):
            return x+y
        v0=0
        x=np.linspace(a, b,1000)

        sol_m1 = odeint(dydx, y0=v0, t=x, tfirst=True)
        sol_m2 = solve_ivp(dydx, t_span=(-10,max(x)), y0=[v0], t_eval=x)
        v_sol_m1 = sol_m1.T[0]
        v_sol_m2 = sol_m2.y[0]
        
        positivey = y_sol[y_sol >0]
            if le


        plt.plot(x,v_sol_m1, label="odeint solution")
        plt.plot(x,v_sol_m2, '--', label="solve_ivp solution")
        plt.legend()
        plt.yscale('log')
        plt.ylabel('$f(x)$')
        plt.xlabel('$x$')
        plt.show()

    elif choice == '2':
    
        def dS_dt(t, S):
            x, y = S
            dx_dt = 5*x-70*y 
            dy_dt = x-y
            
            return [dx_dt, dy_dt]
            

        S0 = [1.5, 0.5] # x(0) = 0, y(0) = 0
        t = np.linspace(a, b, 1000)

        solveivp = bool(input("Do you want to use solve_ivp or odeint to solve this coupled ode? (T/F): "))
        
        if solveivp == True:
            solution = solve_ivp(dS_dt, t_span = (a,b), y0=S0, t_eval=t)
            x_sol,y_sol = solution.y
            
        elif solveivp == False:
            odeintsolution_coupled = odeint(dS_dt, y0=S0, t=t, tfirst=True)
            x_sol = odeintsolution_coupled.T[0] 
            y_sol = odeintsolution_coupled.T[1]
        
        

        plt.plot(t, x_sol, label="$x(t)$")
        plt.plot(t, y_sol, label="$y(t)$")
        plt.yscale('log')
        plt.legend()
        plt.title("Coupled First-Order ODEs")
        plt.show()
