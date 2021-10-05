def bruteForce(p , t ):
    n = len(t)
    m = len(p)
    for i in range(n - m + 1):
        if  p[0] == t[i]:
            for j in range(1 , m + 1 ):
                if p[j] != t[j+ i]:
                    break
                if j == m-1 :
                    return i
    return -1
print(bruteForce('abc', 'ajakljfkalsjdklabc'))