#euler14-Longest Collatz Sequence
chainlist = []
lim = 999999
def collatz():
    counter = 1
    for x in range(2,lim):
        while x != 1:
            if x % 2 == 0:
                x = x/2
                counter += 1
            if x % 2 != 0 and x != 1:
                x = 3*x + 1
                counter += 1
        chainlist.append(counter)
        counter = 1       
collatz()
maxpos = chainlist.index(max(chainlist))
print(maxpos)
