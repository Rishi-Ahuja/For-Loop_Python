#Q1: WAP to print natural numbers till ‘n’. Also , find the sum.

n = int(input('enter n: '))
s = 0

for x in range(1,n+1):
    print(x)
    s+=x
print('sum =', s)
