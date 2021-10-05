import process as  pro
import diff as di
import plus as  pl 

def truFp(p , w  , a , b):
    re = di.diff(p, w, pro.process(p, w, a), pro.process(p, w, b))
    re2 = pl.plus(p, w, re[1], pro.process(p, w,p))
    e = re[0]
    lst_result = re[1]
    if e == 1 or lst_result >=  re2[1]:
        e = re2[0]
        lst_result = re2[1]
    return e , lst_result


print(truFp(2147483647, 8, 38762497, 568424364))