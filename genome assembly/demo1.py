from itertools import permutations


def solve(*strings):
    """
    Given a list of strings, return the shortest string that contains them all.
    """
    return min((simplify(p) for p in permutations(strings)), key=len)

def prefixes(s):
    """
    Return a list of all the prefixes of the given string (including itself),
    in ascending order (from shortest to longest).
    """
    return [s[:i+1] for i in range(len(s))]
  

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

descriptions, ss = parse_fasta(open('D:\python\input.txt', 'r').read().split('\n'))

def simplify(strings):
    """
    Given a list of strings, concatenate them wile removing overlaps between
    successive elements.
    """
    ret = ''
    for s in strings:
        if s in ret:
            continue
        for i, prefix in reversed(list(enumerate(prefixes(s)))):
            if ret.endswith(prefix):
                ret += s[i+1:]
                break
        else:
            ret += s
    return ret

print solve(ss[0],ss[1],ss[2],ss[3])
    










