import urllib2

accessionList=[]
def aaa(acc):
    for i in acc:
        accessionList.append(i)
aaa(open('D:\python\input.txt', 'r').read().split())

def getFromUniprot(filename,accessionList):
    FastaData=''
    for accession in accessionList:
        x=urllib2.urlopen('http://www.uniprot.org/uniprot/'+accession+'.fasta')
        FastaData+=x.read()
        x.close()
    f=open(filename,'w')
    f.write(FastaData)
    f.close

getFromUniprot('D:\python\input.fasta',accessionList)


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

descriptions, ss1 = parse_fasta(open('D:\python\input.fasta', 'r').read().split('\n'))
count=0
for ss in ss1:
   
    print accessionList[count]
    for j in range(len(ss)-2):
        if ss[j]=='N' and ss[j+2] in 'ST' and ss[j+1] not in 'P' and ss[j+3] not in 'P' :
            print j+1,
    count=count+1
    print "\n"
   


