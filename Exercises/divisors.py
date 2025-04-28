n = int(input('Digite a porra de um numero: '))

for i in range(1, n):
    if n % i == 0:
        print(i, 'é divisor de', n)
    