pallist = []
import math


for a in range(500, 1000):
    for b in range(500, 1000):
        c = (a * b)
        f1 = str(c)
        f1 = f1[::-1]
        f1 = int(f1)
        if c == f1:
            pallist.append(c)
print('highest palindrome is:' , max(pallist))
       
        

