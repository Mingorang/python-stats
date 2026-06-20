import random 

runs = 0
nums = []
index = 0

n = int(input("How many samples should there be: "))

while runs <= n:
    number = random.randrange(0,1000,1)
    nums.append(number)
    runs += 1

print(nums)


#for num in nums:
 #   print(num)
  #  index += 1
   # if index > 11:
    #    break
