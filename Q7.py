#Q7: WAP to print the series till ‘n’ terms

n = int(input('enter n: '))

#1 4 7 10 13 16......n
print('pattern 1: ')
y = 1
for x in range(0, n):
    print(y, end = ' ')
    y +=3
print('')

#1 4 9 16 25 36
print('pattern 2: ')
for x in range(1, n+1):
    print(x*x, end=" ")
