a=['19308','16313','16082','16087','19680','18617']
b = [2 * int(x) for x in a]
c = [1, 1, 1, .75, .5, 0]
exp = sum(map(lambda x: x[0] * x[1], zip(b, c)))
print exp

