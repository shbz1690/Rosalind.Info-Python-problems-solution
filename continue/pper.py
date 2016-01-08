from math import factorial

def pper(s):
    n,k=[int(i) for i in s.split()]
    return factorial(n)/factorial(n-k) % 1000000

print pper(open('D:\python\input.txt', 'r').read())
