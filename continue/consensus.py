x = open('D:\python\input.txt', 'r').read() 
seq=''
desc=[]
bases=[]
for l in x:
    if l.startswith('>'):
        desc.append(l)     
    else:
        seq+=l


print desc[0]
print desc[1]
print desc[2]
    

