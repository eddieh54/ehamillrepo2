# variables
facls = []

# factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

x = factorial(100)

# makes a list for ever num in fac(x)
for i in str(x):
    facls.append(i)
    facls = [int(i) for i in facls]

#adds num in fac(x)    
print(sum(facls))

