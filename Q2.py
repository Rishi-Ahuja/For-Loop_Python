#Q2: WAP to print the table of a given number.

n = int(input('enter a number: '))

for x in range(1, 11):
    print(n, 'x', x, '=', n*x)