def problem(n, edges):
    return n - len(edges) - 1



dataset = open('D:\python\input.txt').readlines()
n = int(dataset[0])
edges = []
for i in range(1, len(dataset)):
    edges.append(map(int, dataset[i].split()))
print problem(n, edges)