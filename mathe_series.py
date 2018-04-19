def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def series(n, x):
    i = 0
    s = 0
    while i <= n:
        s += (x ** i) / factorial(i)
        i += 1
    return s


x1 = int(input("Enter value of n i.e. the range: "))
x2 = int(input("Enter a value for x: "))
sum = series(x1, x2)
print(sum)
