# -*- coding: utf-8 -*-
import sys
def locations(s,t):
    results = []
    l = len(t)

    for i in range(len(s) - l):
        if s[i:i+l] == t:
            results.append(i + 1)

    return results

for line in sys.stdin:
    data = open('D:\python\input.txt').read()
    s, t = data.split()
    results = locations(s,t)
print ' '.join(map(str, results))
print