#Q8: WAP to  print the reversed number.

n = int(input('enter a number: '))
rev = 0

for x in range(0, len(str(n))):
    y = n % 10
    rev = rev*10 + y
    n //=10

print(rev)
   