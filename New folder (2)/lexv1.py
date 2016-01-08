with open('D:/python/input.txt') as input_data:
	A, k = [line.strip() for line in input_data.readlines()]
	A = A.split()
	k = int(k)

sets=A
for  l in range(k-1):
    sets = [i+j for i in A for j in [' ']+sets]

for i in sets: print (i)