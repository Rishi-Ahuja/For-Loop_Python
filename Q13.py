#Q13: WAP to print any number ‘a’ raise to the power ‘b’.

a = int(input('enter a: '))
b = int(input('enter b: '))
c = 1

for x in range(0, b):
    c*=a

print(c)