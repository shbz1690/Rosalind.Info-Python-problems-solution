def fact(x):
    f=1
    if x >= 0:
        for i in range(1,x + 1):
            f = f*i
        return f
        
p = []

def allele(s):
    k,n=[int(i) for i in s.split()]
    summ=0
    for i in range(n,((2**k)+1)):
            if i < (2**k +1):
                probability = (fact(2**k)/(fact(i)*fact((2**k)-i)))*(0.25**i)*(0.75**((2**k)-i))
                summ=summ+probability
    print summ

allele(open('D:\python\input.txt', 'r').read())