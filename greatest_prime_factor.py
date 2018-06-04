# Largest prime factor

num = int(input("Enter a number: "))
factors = []
prime = []

for i in range(2, num // 2 + 1):
    if num % i == 0:
        factors.append(i)


def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


factors.append(num)


print("The factors are: ", factors)

for no in factors:
    if isPrime(no):
        prime.append(no)

print("The Greatest Prime Integer of ", num, "is: ", max(prime))
