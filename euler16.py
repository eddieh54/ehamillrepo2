x = 2**1000
numlist = []

for i in str(x):
    numlist.append(i)
    numlist = [int(i) for i in numlist]

print('The number is:' + str(x))
print('The sum of its digits is:' + str(sum(numlist)))   

