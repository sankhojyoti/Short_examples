a = 1
b = 1
c = 0
i = 1
fib = []
sum = 0

while b in range(1, 4000000):
    fib.append(b)
    b, a = a + b, b
print(fib)

while i in range(1, len(fib)):
    sum += fib[i]
    i += 3
print(sum)
