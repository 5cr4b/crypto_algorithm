import math
import process as  pro

def multi(p , w , lst_A , lst_B):
    m = math.ceil(math.log(p , 2 ))
    t = math.ceil(m / w )
    c = [0] * w 
    for i in range(len(lst_A)):
        u = 0
        for j in range(len(lst_B)):
            uv = c[i + j ] + lst_A[i] * lst_B[j] + u
            u = int(uv / pow( 2 , w))
            v = uv % pow(2 ,w )
            c[i + j ]  = v
        c[i + t ] = u
    c.reverse()
    return c
            
print(multi(2147483647 , 8 , pro.process(2147483647, 8,524647) , pro.process(2147483647, 8, 32549)))