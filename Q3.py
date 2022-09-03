#Q3: WAP to input any number and print its factorial.

n = int(input('enter n: '))
f = 1

for x in range(1, n+1):
    f *= x

print('factorial =', f)