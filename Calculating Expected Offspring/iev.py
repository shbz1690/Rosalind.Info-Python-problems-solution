def offspring(s):
    
    value=[int(i) for i in s.split()]
    return (2*value[0] + 2*value[1] + 2*value[2] + 1.5*value[3] + 1*value[4] + 0*value[5])

print offspring(open('D:\python\input.txt', 'r').read())

