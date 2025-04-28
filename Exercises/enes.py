n = int(input('Digite a quantidade de loop: '))
contOdd = 0
sumEven = 0

for i in range(n):
    num = int(input('Digite um numero: '))

    if num % 2 != 0:
        contOdd += 1
    else:
        sumEven += num

print(contOdd)
print(sumEven)
