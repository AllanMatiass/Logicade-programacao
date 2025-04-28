# selection -> if
# rep -> for/while

# Leia 15 numeros e imprima o maior

maxN = float(input('Digite o numero: '))
counter = 0

while counter < 15:
    jaguare = float(input('Digite o numero: '))
    
    if jaguare > maxN:
        maxN = jaguare
    counter += 1

print(maxN)