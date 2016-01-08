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

import urllib
code = "Q7Z7W5"
data = urllib.urlopen("http://www.uniprot.org/uniprot/" + code + ".txt").read()

for protein_name in f:
	protein_url = 'http://www.uniprot.org/uniprot/'+protein_name.strip()+'.fasta'
	protein_fasta = ReadFASTA(protein_url)
	locations = ''
	for i in range(0, len(protein_fasta[0][1])-4+1):
		# Check for the N-glycosylation motif is written as N{P}[ST]{P}.
		if (protein_fasta[0][1][i] == 'N') and (protein_fasta[0][1][i+1] != 'P') and (protein_fasta[0][1][i+2] in ['S','T']) and (protein_fasta[0][1][i+3] != 'P'):
			locations += str(i+1)+' '
        
	if locations != '':
		print protein_name.strip()
		print locations.strip()
		if not line_written:
			output_file.write(protein_name.strip()+'\n'+locations.strip())
			line_written = True
		else:
			output_file.write('\n'+protein_name.strip()+'\n'+locations.strip())