def phanTichThuaSoNguyenTo(n):
    coso = []
    somu = []
    count = 0
    i = 2 
    while n >1 :
        while n % i == 0:
            n = n / i
            count += 1 
        if count >= 1 :
            coso.append(i)
            somu.append(count)
            count = 0
        i += 1  
    return coso , somu
print(phanTichThuaSoNguyenTo(int(input("n = "))))