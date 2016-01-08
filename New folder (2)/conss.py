def cons_preproc(s):
	return s.lower().split("\n")

def cons(matr):
	#profile matrix
	prof = {"a" : [], "c" : [], "g" : [], "t" : []}
	#consensus string
	cons = ""
	# calculating row's length
	length = len(matr[0])
	for key in prof:
		for i in range(length):
			prof[key].append(0)

	# calculating profile matrix
	for row in range(len(matr)):
		for col in range(length):
			prof[matr[row][col]][col] += 1

	# calculating consensus
	mask = []
	for i in range(length):
		mask.append(("a", 0))

	for key in prof:
		for i in range(len(prof[key])):
			if prof[key][i] > mask[i][1]:
				mask[i] = key, prof[key][i]

	for letter, val in mask:
		cons += letter

	# output
	print(cons.upper())

	for key in prof:
		print "%s: " % key.upper(),
		for val in prof[key]:
			print "%d" % val,
		print()

	return (cons, prof)