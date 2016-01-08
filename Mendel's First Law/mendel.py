def abc(k, m, n):
    value = ((k*k - k) + 2*(k*m) + 2*(k*n) + (.75*(m*m - m)) + 2*(.5*m*n))/((k + m + n)*(k + m + n -1));
    return value
    

sol= abc(28,28,28)
print sol