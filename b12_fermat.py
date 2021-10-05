import random
def  modPower(a , b , n):
    if b == 1:
        return a
    else :
        x = modPower(a, int(b/2), n)
        if b % 2 == 0:
            return (x * x ) % n
        else:
            return (x * x * a ) % n

def  gcd(a  , b):
    if  b ==  0:
        return a 
    return gcd(b , a %b)

def fermat(n):
    a = random.randint(2, n-1)
    if gcd(a , n) != 1:
        return "HopSo"
    elif modPower(a, n-1, n) != 1:
        return "HopSo"
    else:
        return "NguyenTo"
print(fermat(20))
    
    