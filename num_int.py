import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.integrate import simpson as simps
from scipy.integrate import quad
import sys


def reasonable_function(expression):
    allowed = {
        "exp": np.exp,
        "e": np.e,
        "pi": np.pi,
        "sqrt": np.sqrt,
        "sin": np.sin,
        "cos": np.cos,
        "tan": np.tan,
        "csc": np.asin,
        "sec": np.acos,
        "cot": np.atan,
        "sinh": np.sinh,
        "cosh": np.cosh,
        "tanh": np.tanh,
        "loge": np.log,
        "log": np.log10,
    }
    def f(x):
        return eval(expression, {**allowed}, {"x": x})
    return f
def sample_function(f, a, b, dx):

    x = np.arange(a, b + dx, dx)

    with np.errstate(divide='ignore', invalid='ignore', over='ignore'):
        y = f(x)

    valid = np.isfinite(y)

    x = x[valid]
    y = y[valid]

    return x, y


def detect_singularities(x, y, alpha):
    lower = np.percentile(y, 100 - alpha)
    upper = np.percentile(y, alpha)
    outliers = (y < lower) | (y > upper)
    gradient = np.abs(np.diff(y))
    gradient_limit = np.percentile(gradient, alpha)
    regions = []
    inside = False
    for i in range(len(gradient)):
        if outliers[i] and gradient[i] > gradient_limit:
            if not inside:
                start = i
                inside = True
        else:
            if inside:
                end = i
                regions.append((x[start], x[end]))
                inside = False
    if inside:
        regions.append((x[start], x[-1]))
    return regions
def split_intervals(a, b, regions, dx):
    intervals = []
    current = a
    gap = 5 * dx
    for left, right in regions:
        if left - gap > current:
            intervals.append((current, left - gap))
        current = right + gap
    if current < b:
        intervals.append((current, b))
    return intervals
def main():
       #Initialising variables
        print("Approximating integrals with rectangles")    
        expr = input("Integral as a function of x: ")
        a = float(input("lower limit: "))
        b= float(input("upper limit: "))
        dx = float(input("width of rectangle: "))
        #larger alpha gives little to no divergent points
        alpha = float(input("measure for finding singularities: (85<=alpha<100): "))
        if alpha<85 or alpha>=100:
            sys.exit("You know this value isnt allowed.")
        else:
            pass
        #Riemann sum
        f = reasonable_function(expr)
        x_rect, y_rect = sample_function(f,a,b,dx)
        area = np.sum(y_rect * dx)
        
        
        #calculating % error(s) and simpson function
        x, y = sample_function(f,a,b,dx)
        regions = detect_singularities(x,y,alpha)
        intervals = split_intervals(a,b,regions,dx)
        #actual function
        for left, right in intervals:
          x_plot, y_plot = sample_function(f, left, right, dx)
             #Actual integral
        actual_area = 0
        for left, right in intervals:
          actual_area += quad(f,left,right)[0]
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
        print("")
        print(f"However, the actual integral is: {actual_area.__round__(9)}")
        print("")
        if error_simpsons > 100 or error_riemann>100 :
            error_simpsons = 100
            error_riemann = 100
        print(f"Riemann's is {100-error_riemann}% accurate,  Simpson's is {100-error_simpsons}% accurate")
        if error_simpsons < error_riemann:
             print("Simpson's rule give a more accurate answer")
        elif error_riemann < error_simpsons:
             print("Riemann's is more accurate,")
        else:
             print("No value to compare to.")
             print("For this to be outputted function is most likely divergent.")
        time.sleep(3)
        plt.draw()
        plt.pause(600)


if __name__ == "__main__":
    main()