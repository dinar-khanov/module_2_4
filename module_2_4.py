numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers.remove(1)
primes = []
not_primes = []
for i in numbers:
    is_Prime = True
    for j in range(2, i):
        if i % j == 0:
            is_Prime = False
            break
    if is_Prime:
        primes.append(i)

    else:
        not_primes.append(i)
print("Primes: ",primes)
print("Not primes: ",not_primes)