operator = False
t = 0
for i in range(1, 11):
    divisor = i * i
    if operator:
        s = i / divisor
        t += s
    else:
        s = i / divisor
        t -= s
    
    operator = not operator

print(t)