
def gcd(a , b ):
    if b == 0:
        return a 
    return gcd(b , a% b)

def pollard(n ):
    a = 2 
    b = 2 
    while 1 :
        a = (a* a + 1) % n
        b= (b * b + 1 )  %  n
        b= (b * b + 1 )  %  n       
        d = gcd(a - b , n)
        if 1 < d < n:
            return d 
        if d == n :
            return 'failed'
print(pollard(20))