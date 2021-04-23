# variables 
x = 2**1000
numlist = []
# makes a list of the num in x, and converts it to int
for i in str(x):
    numlist.append(i)
    numlist = [int(i) for i in numlist]
# finds the sum of the list
print('The number is:' + str(x))
print('The sum of its digits is:' + str(sum(numlist)))   

