import sys
def hamming_distance(s, t):
    dh = 0

    for i, c in enumerate(s):
        if c != t[i]:
            dh += 1
 
    return dh
    
for line in sys.stdin:    
    data = open('D:\python\input.txt').read()
    s, t = data.split()
    dist = hamming_distance(s, t)
print dist
print