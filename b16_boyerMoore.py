def last_occured(p , x):
    for i in range(len(p) - 1, -1 , -1 ):
        if  p[i ] == x :
            return i
    return -1

def boyer_moore(p , t ):
    n = len(t)
    m = len(p)
    i = m -1 
    j = m -1
    while i < n:
        if p[j] != t[i]:
            i = i + m - min(j , last_occured(p , t[i]))
            j = m -1
        else:
            if  j == 0:
                return i
            i -= 1 
            j -= 1
    return -1
print(boyer_moore('abc', 'kajdklsajdklabc'))