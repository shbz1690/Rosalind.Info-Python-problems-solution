from math import factorial
n=1802
m=1238
summ=0
for i in xrange(m,n+1):
    a=factorial(n)/(factorial(i)*factorial(n-i))
    summ=summ+a
print summ%1000000