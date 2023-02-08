def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

numbers = list(map(int,input().split()))
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)
