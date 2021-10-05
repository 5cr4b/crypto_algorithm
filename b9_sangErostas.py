def sangEratos(n):
    not_prime = []
    is_prime = []
    
    for i in range(2 , n):
        if i not in not_prime:
            is_prime.append(i)
            for j in range(i , n+ 1, i ):
                not_prime.append(j)
    return is_prime
print(sangEratos(100))