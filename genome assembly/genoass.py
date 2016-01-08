import itertools as it

def abc():
    seqs = ['AGG', 'AGT', 'CCG', 'CGT', 'GAG', 'GGA', 'GGT', 'GTA', 'GTG', 'TAG', 'TGG']
    seq_perms = [''.join(perm) for perm in it.permutations(seqs)]
    for i in range(0, len(''.join(seqs))):
        seq_perms = [''.join(perm)[:i] for perm in it.permutations(seqs)]   
        for perm in seq_perms:   
            if all(perm.find(seq) != -1 for seq in seqs) == True:
                print 'Shortest superstring containing all strings:\n{}'.format(perm)
                return 

p=abc()
print p