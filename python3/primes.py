primes = [2]
for i in range(3, 100000): # Incorrect range!
    is_prime = True
    for j in range(0, len(primes)):
        p = primes[j]
        if j*j > i:
            break
        if p % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
