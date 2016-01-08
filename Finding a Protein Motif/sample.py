import urllib2
import re

def getFromUniprot(filename,accessionList):
    """Get a set of protein sequenses from the UniProt database"""
    FastaData=''
    for accession in accessionList:
        x=urllib2.urlopen('http://www.uniprot.org/uniprot/'+accession+'.fasta')
        FastaData+=x.read()
        x.close()
    f=open(filename,'w')
    f.write(FastaData)
    f.close

getFromUniprot('D:\python\input.fasta',['A2Z669','B5ZC00',
        'P07204_TRBM_HUMAN','P20840_SAG1_YEAST'])


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

mos = [x for x in re.finditer(r'(?=(N[^P][ST][^P]))',  str(sequences[0]))]

print mos
print(' '.join([str(mo.start(0) + 1) for mo in mos]))
