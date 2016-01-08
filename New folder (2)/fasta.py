
accessionList=[]
def aaa(acc):
    for i in acc:
        accessionList.append(i)
aaa(open('D:\python\input.txt', 'r').read().split())
print accessionList