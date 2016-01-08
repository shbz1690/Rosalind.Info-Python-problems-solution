gap = [1, 1]
def fib(n, m):
    inc = 2
    while (inc < n):
        if (inc < m):
            gap.append(gap[-2] + gap[-1])
        elif (inc == m or inc == m+1):
            gap.append((gap[-2] + gap[-1]) - 1)
        else:
            gap.append((gap[-2] + gap[-1]) - (gap[-(m+1)]))
        inc += 1
    return (gap[-1])


print (fib(89, 19))