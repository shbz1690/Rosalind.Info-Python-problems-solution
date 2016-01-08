import re

data_file = open("D:\python\input.fasta","r")
data=data_file.read()
org=re.findall(r'>(\w*)',data)
seq=[i.replace('\n','') for i in re.split(r'>\w*',data,re.DOTALL)[1:]]
print org
print seq 