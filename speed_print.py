import time 
import random
import math
alpha = []
for a in range(0,100):
    beta=[]
    upper=int(random.randrange(0,10**3,1))/(10**6)
    for i in range(0,10):
        start = time.time()


        k=0
        while (time.time()-start) < upper:
            k+=1
            pass
        beta.append(k.__trunc__())
        #print(f"Number reached in: {time.time()-start:.6} seconds is {k}")
        i+=1

    #print(sum(beta))
    print(f"Mean numbers printed per second is {sum(beta)/upper}")
    alpha.append(sum(beta)/upper)

print(max(alpha))
#Need to add matplot lib and difficult part will be introducing regressions, adding a list of reasonable methods similar to lines 9-25 of num_int.
