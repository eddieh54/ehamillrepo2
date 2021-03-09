import math
import time
starttime = time.time()
triplist = []
for a in range(200 , 1000):
    for b in range(200 , 1000):
        for c in range(200 , 1000):
            if a < b and b < c:
                if a**2 + b**2 == c**2:
                    if a + b + c == 1000:
                        triplist.append(a)
                        triplist.append(b)
                        triplist.append(c)
                        print(math.prod(triplist))
                        print('time:',time.time() - starttime)


                
