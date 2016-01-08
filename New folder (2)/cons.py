class FASTA:
    def __init__(self, name, data):
        self.name = name
        self.data = data

def get_char_profile(FASTAS, char):
    n = len(FASTAS[0].data)
    profile = []
    for i in range(0, n):
        profile.append(0)
    for F in FASTAS:
        data = F.data
        for j in range(0, len(data)):
            if data[j] == char:
                profile[j] += 1
    return profile


dataset = []
lines = list(open("D:/python/input.fasta"))
for i in range(0, len(lines)-1, 2):
    name = lines[i].rstrip()
    data = lines[i+1].rstrip()
    dataset.append(FASTA(name, data))

nucleotides = 'ACGT'
profile_matrix = []
for ch in nucleotides:
    profile_matrix.append(get_char_profile(dataset, ch))
cols = len(dataset[0].data)
rows = len(profile_matrix)
cons_string = ""
for i in range(0, cols):
    consensus = nucleotides[0]
    highest = 0
    for j in range(0, rows):
        if profile_matrix[j][i] > highest:
            consensus = nucleotides[j]
            highest = profile_matrix[j][i]
    cons_string += consensus

print cons_string
for i in range(0, len(nucleotides)):
    print nucleotides[i] + ": " + " ".join(map(str, profile_matrix[i]))