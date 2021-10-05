def nghichDao(a, b):
    x1 = 1
    x2 = 0
    while b!= 1:
        q = int(a / b)
        r = a % b
        x = x2 - x1*q
        a = b
        b = r
        x2 = x1
        x1 = x
    return x1
         
    

print(nghichDao( 489573857,45682375))
