def reverse(perm, start, end):
	revperm = perm[:]
	for i in range(start, end + 1):
		revperm[i] = perm[end + start - i]
	return revperm

# returns count of different numbers at similar positions
# between alpha and beta
def diff(alpha, beta = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
	count = 0
	for i in range(len(alpha)):
		if alpha[i] != beta[i]:
			count += 1
	return count

# finds permutation with minimum distance between curperm and target
def find_min(curperm, target = [1,2,3,4,5,6,7,8,9,10]):
	newperm = []
	min_dist = len(target) + 1
	for i in range(0, len(target) - 1):
		for j in range(1, len(target) - i):
			tmp = reverse(curperm[:], i, i+j)
			if diff(tmp, target) < min_dist:
				newperm = tmp
				min_dist = diff(tmp, target)

	return newperm

def rear(path):
	perm_list = []

	i = 0
	for line in open(path):
		tmp = []
		for ch in line.split(" "):
			try:
				tmp.append(int(ch))
			except:
				continue
		if tmp:
			perm_list.append(tmp)

	tmp = []
	for i in range(0, len(perm_list), 2):
		tmp.append((perm_list[i], perm_list[i+1]))
	perm_list = tmp[:]
	#return perm_list

	# check all variants of reversing
	# and find one with less distance between this pair
	t = 2
	perm = perm_list[t][0]
	mem = perm[:]
	target = perm_list[t][1]
	while diff(mem, target) > 0:
	   mem, dist = find_min(mem, target)
	   print dist,
	   print(mem)
	return mem
