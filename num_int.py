import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.integrate import simpson as simps
from scipy.integrate import quad


def reasonable_function(expression):
    allowed = {
    "exp" : np.exp,
    "e"   : np.e,
    "pi"  : np.pi,
    "sqrt": np.sqrt,
    "sin" : np.sin,
    "cos" : np.cos,
    "tan" : np.tan,
    "csc" : np.asin,
    "sec" : np.acos,
    "cot" : np.atan,
    "sinh": np.sinh,
    "cosh": np.cosh,
    "tanh": np.tanh,
    "log" :np.log10,
    }
    def f(x):
        return eval(expression, {**allowed}, {"x": x})
    return f
def main():
       #Initialising variables
        print("Approximating integrals with rectangles")
        expr = input("Integral as a function of x: ")
        a = float(input("lower limit: "))
        b= float(input("upper limit: "))
        dx = float(input("width of rectangle: "))

        #Riemann sum
        f = reasonable_function(expr)
        x_rect = np.arange(a,b,dx)
        y_rect = f(x_rect)
        area = np.sum(y_rect * dx)
        
        #actual function
        x_plot = np.linspace(a,b, int((b-a)/dx))
        y_plot = f(x_plot)

        #Actual integral
        actual_area = quad(f,a,b)[0]

        #calculating % error(s)
        x = np.linspace(a,b,(int((b-a)/dx)))
        y = f(x)
        sim = simps(y,x)
        error = 100*(abs(sim-area)/sim)
        error_simpsons = 100*((abs(sim-actual_area))/actual_area)
        error_riemann = 100*((abs(actual_area-area))/actual_area)

        #Plotting results
        plt.figure(figsize=(10,6))
        plt.plot(x_plot,y_plot, color="red", label=f"y = {expr}")
        plt.bar(x_rect,y_rect,color="lightblue",edgecolor="black",  label="Rectangles", width = dx, align="edge")
        plt.axhline(0,color="black", linewidth=0.1)
        plt.title("Integral approximation with rectangles")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)

        print(f"Simpson's rule gave an integral of {sim}, Riemann's sum from {a} to {b} gives {area.__round__(11)}, so the % error between the two approximations  is: {error}% ")
        print(f"However, the actual integral is: {actual_area.__round__(9)}")
        print(f"Riemann is {100-error_riemann} accurate,  Simpson's is {100-error_simpsons} accurate")
        if error_simpsons < error_riemann:
             print("Simpson's rule give a more accurate answer")
        else:
             print("Riemann's is more accurate,")
        
        time.sleep(30)
        plt.draw()
        plt.pause(100)


if __name__ == "__main__":
    main()
