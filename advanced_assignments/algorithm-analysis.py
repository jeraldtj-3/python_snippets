# complexity of O(n) 
def sum_n(n): 
    sum_total = 0 
    for i in range(1,n+1): 
        sum_total+=i  
    return sum_total 

# importing time module for computing the running time 
import time   
start_time = time.time()   
end_time = time.time()   
total_time = end_time-start_time


# has comoplexity T(n) = 3n**2 + 2n + 4 
# 3 assignment statements inside the double for loop Ie. 3n**2
# total 4 simple assignment statements Ie. 4 
# single forloop and two assignment statements inside it Ie. 2n 
a = 5 
b = 4 
c = 10 
for i in range(a): 
    for j in range(b): 
        x = i*i 
        y = j*j  
        z = i*j
        
for k in range(a): 
    w = a*k+45  
    v  = b*b  
d = 33
