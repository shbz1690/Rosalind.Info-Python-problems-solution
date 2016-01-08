def fasta_records(file_name):
    ''' Returns a list of (name, seq) pairs for fasta records in file_name. '''
    records = []
    fh = open(file_name)
    name = fh.readline().strip().lstrip('>')
    while name:
        seq = ''
        line = fh.readline().strip()
        while line and not line.startswith('>'):
            seq += line
            line = fh.readline().strip()
        records.append((name, seq))
        name = line.lstrip('>')
    return records
    


file_name = 'D:\python\solutions\input.fasta'
records = fasta_records(file_name)

for name, seq in records:
    print name
    print seq
    print
    


test_seq = 'GCATATATGCTAG'
gcs = [char for char in test_seq if char == 'G' or char == 'C']

gc_count = sum(1 for char in test_seq if char == 'G' or char == 'C')


def gc_content(seq):
    ''' Returns the GC content of seq as a percentage. '''
    gc_count = sum(1 for char in seq if char == 'G' or char == 'C')
    return 100 * float(gc_count) / len(seq)

records_gc = [(name, gc_content(seq)) for name, seq in records]
name, gc = max(records_gc, key=lambda (name, gc): gc)
