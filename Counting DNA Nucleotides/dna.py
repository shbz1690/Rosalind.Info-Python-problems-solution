import sys

for seq in sys.stdin:
    for i in ('ACGT'):
        print seq.count(i),
        
print