import diff as di
import plus as pl 
import process as pro

def congFp(p , w , a , b ):
    re = pl.plus(p , w , pro.process(p , w ,a) , pro.process(p , w , b))
    re2 = di.diff(p , w , re[1] , pro.process(p , w  ,p))
    e = re[0]
    lst_result = re[1]
    
    if e == 1 or lst_result < pro.process(p , w ,p ):
        e = re2[0]
        lst_result = re2[1]
    return e , lst_result
    
    
print(congFp(2147483647, 8 ,2147483646,  2147483643))