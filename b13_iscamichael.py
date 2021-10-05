import math
def gcd(a ,  b):
    if b ==  0 :
        return  a 
    return  gcd(b ,  a % b)

def is_prime (n):
    if n < 2 :
        return False
    for i in range(2  ,  math.ceil(math.sqrt(n))):
        if n % i == 0 :
            return False
    return True

def is_camichael(n):
    if is_prime(n) or n <  2:
        return False
    for i in range(n):
        if gcd(i, n) == 1 :
            if pow(i , n-1) % n != 1 :
                return False
    return True
print(is_camichael(5611))