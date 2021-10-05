import math
def gcd(a , b ):
    if b == 0 :
        return a 
    return gcd(b , a%b)

def is_pirme(n):
    if n < 2 :
        return False
    for i in range(2 , math.ceil(math.sqrt(n))):
        if n % i == 0 :
            return False
    return True
def is_camichael(n):
    if is_pirme(n) or n < 2:
        return False
    for i in range(n):
        if gcd(i, n) == 1:
            if  pow(i , n-1) % n != 1:
                return False
    return True
for i in range(10000):
    if is_camichael(i):
        print(i)