def sangEratos(n):
    is_prime = []
    not_prime = []
    i =  2 
    for i in range(2,n+1):
        if i not in is_prime:
            is_prime.append(i)
            for j in range(i,n+1,n):
                not_prime.append(j)