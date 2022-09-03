#Q5: WAP to print Fibonacci series till given number ‘n’.

n = int(input("enter n: "))

x, y = 1, 1
print(x, y, end=' ')

for i in range(0, n-2):
    z = x + y
    print(z, end=' ')
    x = y
    y = z