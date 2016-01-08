aa_mass = {'E': 129.04259,'H': 137.05891,'L': 113.08406,'N': 114.04293,'R': 156.10111, 'Y': 163.06333, 'V': 99.06841,
                            'A': 71.03711,'F': 147.06841, 'M': 131.04049, 'K': 128.09496, 'Q': 128.05858,'S': 87.03203,'P': 97.05276,
                            'C': 103.00919,'G': 57.02146,'D': 115.02694,'I': 113.08406,'T': 101.04768,'W': 186.07931}

mass = open('D:/python/input.txt').read().strip()
s_value = map(float, mass.split())
ll=len(s_value)

def spec(s):
    result = ''
    sets = {}
    for i, j in aa_mass.iteritems():
        sets[round(j, 4)] = i

    for i in range(1,ll ):
        x = s_value[i - 1]
        y = s_value[i]
        result += sets[round(y - x, 4)]
    return result
print spec(mass)