def parse_fasta (lines):
    descs = []
    seqs = []
    data = ''
    for line in lines:
        if line.startswith('>'):
            if data:
                seqs.append(data)
                data = ''
            descs.append(line)
        else:
            data += line.rstrip('\r\n')
    seqs.append(data)
    return descs, seqs

descriptions, dna = parse_fasta(open('D:\python\input.fasta', 'r').read().split('\n'))


def lcs(s1, s2):
    matrix = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i][j - 1], matrix[i - 1][j])
    return matrix
                
def search(matrix, s1, s2, i, j):
    finalString = ""
    while i != 0 and j != 0:
        if matrix[i][j] == matrix[i - 1][j]:
            i -= 1
        elif matrix[i][j] == matrix[i][j - 1]:
            j -= 1
        else:
            finalString = s1[i - 1] + finalString
            i -= 1
            j -= 1
    return finalString
        
matrix = lcs(dna[0], dna[1])
print(search(matrix, dna[0], dna[1], len(dna[0]), len(dna[1])))