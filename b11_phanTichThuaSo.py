def phanTich(n):
    coso = []
    somu = []
    count = 0
    i = 2
    while n > 1 :
        while n % i == 0:
            count += 1 
            n = int(n / i)
        if count > 0:
            coso.append(i)
            somu.append(count)
            count = 0
        i += 1 
    return coso , somu
print(phanTich(20))