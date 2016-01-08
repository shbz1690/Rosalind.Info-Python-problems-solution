import sys
dataset=[]
for l in sys.stdin.read().split():
    dataset.append(int(l))


n = 8525
d = [(0, -1)]*n 
for i in range(n-1, -1, -1):
    bb = 0
    indexx = -1
    for j in range(i+1, n):
        if dataset[i] < dataset[j] and d[j][0] + 1 > bb:
            bb = d[j][0] + 1
            indexx = j
    d[i] = (bb, indexx)
    
result = []
indexx = max(range(n), key=lambda i: d[i][0])
def LongdecSeq(data):
  m = [0] * n 
  for i in range( n - 1, -1, -1 ):
    for j in range( n - 1, i, -1 ):
      if m[i] <= m[j] and data[i] > data[j]:
        m[i] = m[j] + 1
  max_value = max( m )
 
  result1 = []
  for i in range( len( m ) ):
    if max_value == m[i]:
      result1.append(data[i])
      max_value -= 1
 
  return result1
while indexx != -1:
    result.append(dataset[indexx])
    _, indexx = d[indexx]
a=result
print ' '.join(str(p) for p in a)
b=LongdecSeq(dataset)
print ' '.join(str(p) for p in b)