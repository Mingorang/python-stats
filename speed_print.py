import time 

start = time.time()
k = int(input("Choose a number: "))
for i in range(0,10**k):
    print(i)
    i+=1
end = time.time()