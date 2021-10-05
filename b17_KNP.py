def lps(p):
    m = len(p)
    arr = [0] * m
    i = 1 
    j = 0 
    while i < m:
        if p[j] == p[i]:
            j+= 1  
            arr[i] = j
            i += 1 
        else:
            if j != 0 :
                j = arr[j-1]
            else:
                arr[i] = 0
                i += 1 
    return arr
def kmp(p , t):
    arr = lps(p)
    n = len(t)
    m = len(p)
    i = 0 
    j = 0
    while i < n:
        if p[j] == t[i]:
            i += 1
            j += 1
        if j == m :
            return i - j
        elif i < n  and  p[j] != t[i]:
            if j != 0 :
                j = arr[j-1]
            else:
                i  += 1
print(kmp('abc', 'jflkajslabc'))