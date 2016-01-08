def lengthGenerate(s1, s2):
    rs1 = range(len(s1))
    rs1.reverse()

    rs2 = range(len(s2))
    rs2.reverse()

    L = []

    for i in range(len(s1)+1):
        L.append([])
        for j in range(len(s2)+1):
            L[i].append(0)

    for i in rs1:
        for j in rs2:
            if(s1[i] == s2[j]):
                L[i][j] = 1 + L[i+1][j+1]
            else:
                L[i][j] = max(L[i+1][j], L[i][j+1])

    return L

def genSeq(L, s1, s2):
    m = L[0][0]
    last = m

    S = ""

    i,j = 0,0

    while len(S) < m:
        if(s1[i] == s2[j]):
            S = S+s1[i]
            i = i + 1
            j = j + 1
        elif L[i+1][j] >= L[i][j+1]:
            i = i + 1
        else:
            j = j + 1

    return S

def runLab():
    str = raw_input()
    l = str.split("\n")

    s1 = min(l)
    s2 = max(l)

    L = lengthGenerate(s1, s2)


    print genSeq(L, s1, s2)