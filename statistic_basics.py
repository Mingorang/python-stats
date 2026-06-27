import random 
import math
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
import matplotlib.widgets



#Used for running loops from sample size
runs = 0
nums = []
nums2 = []
index = 0

n = int(input("How many samples should there be: "))
a=0
b= int(input("Change the upper limit of the 'random' distribution of numbers: ")
while runs <= (n-1):
    number = random.randrange(a,b,1)
    nums.append(number)
    nums2.append(number*number)
    runs += 1


mean = sum(nums)/n
sum(nums2)
std = math.sqrt((sum(nums2)/n)  - (mean*mean))
print("mean is: ", mean.__round__(4))
print("standard deviation is: ", std.__round__(4))

x=np.linspace(a, b,n)
y=norm(loc=mean, scale = std).pdf(x)
fig,ax = plt.subplots(figsize=(20, 10))
ax.set_snap(True)
cursor = matplotlib.widgets.Cursor(ax, useblit=True, horizOn=True, vertOn=True, color="lightgreen")

fig.canvas
plt.plot(x,y)
plt.show()
