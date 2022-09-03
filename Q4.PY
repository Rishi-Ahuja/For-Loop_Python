#Q4: WAP  to print odd numbers till a given number ’n’ and find their sum.

n = int(input('enter a natural no.'))
s = 0

for x in range(1, n+1, +2):
    print(x)
    s+=x

print('sum = ', s)
