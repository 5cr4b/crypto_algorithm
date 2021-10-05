import math
def process( p , w , ab):
    m = math.ceil(math.log(p , 2))
    t = math.ceil(m / w)
    lst = []
    for i in range(t):
        result = ab // pow( 2  , w * (t -1 -i)) 
        lst.append(result)
        ab_1  = result * pow(2 , w * (t -1 - i))
        ab = ab - ab_1
    lst.reverse()
    return lst

