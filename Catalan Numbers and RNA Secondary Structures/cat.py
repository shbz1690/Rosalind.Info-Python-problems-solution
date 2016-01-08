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

descriptions, sequences = parse_fasta(open('D:\python\input.fasta', 'r').read().split('\n'))

s=sequences[0]

ab = [[-1 for x in range(1000)] for y in range(1000)]

def cata(s, x, y):
  if x >= y:
    ab[x][y] = 1
    return 1
  if ab[x][y] != -1:
    return ab[x][y]
  ab[x][y] = 0
  for j in xrange(x + 1, y + 1, 2):
    if (s[x] + s[j]) in ["AU", "UA", "GC", "CG"]:
      d = cata(s, x + 1, j - 1) * cata(s, j + 1, y)
      ab[x][y] = (ab[x][y] +  d) % 1000000
  return ab[x][y]

print (cata(s, 0, len(s) -1))