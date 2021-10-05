def nhanBinhPhuongCoLap(a, k, n):
    b = 1
    if k == 0:
        return b
    binaryK = []
    tmp = k
    while tmp > 0:
        binaryK.append(int(tmp%2))
        tmp = int(tmp/2)
    if binaryK[0] == 1:
        b = a
    for i in range(1,len(binaryK)):
        a = (a*a) % n
        if binaryK[i] == 1:
            b = (a*b) % n
    return b

def  miller_rabin(n):
    if n < 2  :
        return "hopSo"
    if n- 2 < 2 :
        return 'Nguyen To'
    s = 0 
    k = n  -1 
    while k % 2 == 0:
        k /= 2 
        s += 1 
    t = int(input("nhap so lan thu : "))
    while t < 1 or t  > n - 2 :
        t = int(input())
    for i in range(2 ,t + 2):
        r = nhanBinhPhuongCoLap(i, k, n)
        if r != 1 and  r != n - 1 :
            j  = 1
            while j <= s - 1  and r != n-1:
                r = r * r % n  
                if r == 1 :
                    return 'hopSo'
                j += 1 
            if r != n -1 :
                return 'hopSo'
    return 'nguyenTo'
print(miller_rabin(97))
            
