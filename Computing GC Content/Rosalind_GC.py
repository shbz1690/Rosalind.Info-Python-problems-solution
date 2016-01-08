def fasta_records(my_seq):
    records = []
    f = open(my_seq)
    name = f.readline().strip().lstrip('>')
    while name:
        seq = ''
        line = f.readline().strip()
        while line and not line.startswith('>'):
            seq += line
            line = f.readline().strip()
        records.append((name, seq))
        name = line.lstrip('>')
    return records

my_seq = 'D:\python\input.txt'
records = fasta_records(my_seq)

def gc_content(seq):
    gc_count = sum(1 for char in seq if char == 'G' or char == 'C')
    return 100 * float(gc_count) / len(seq)
records_gc = [(name, gc_content(seq)) for name, seq in records]
name, gc = max(records_gc, key=lambda (name, gc): gc)
print name
print gc
print