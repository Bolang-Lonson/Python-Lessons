def is_prime(num):
    count = 0
    for j in range(2, num):
        if num % j == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False

prime_nums = [i for i in range(2,1000) if is_prime(i)]
print(prime_nums)
