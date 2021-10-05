import math
def diff(p , w, lst_A , lst_B , ):
    m = math.ceil(math.log(p , 2 ))
    t =  math.ceil(m / w)
    lst_result = []
    e =  0
    for i in range(t):
        result = lst_A[i] - lst_B[i] - e 
        if result < 0:
            e = 1 
            result = result % pow(2, w )
        else:
            e = 0
        lst_result.append(result) 
    return [e , lst_result]