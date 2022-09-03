#Q10: WAP to print the sum of the series till ‘n’ terms:-

n = int(input('enter n: '))
x = int(input('enter x: '))
print('\n')

#s = x + x^2 + x^3 …
sum = 0
for i in range(1, n + 1):
    sum = sum + (x**i)
    print(x**i, end = ' ')
print('\nsum =', sum)
print('\n')

#s = x + x^3 + x^5
summ = 1
for i in range(1, n + 1):
    summ = summ + (x**(2*i-1))
    print(x**(2*i-1), end = ' ')
print('\nsum =', summ)
print('\n')

#s = 1 + x/1! + x^2/2!…
sun = 0
for i in range(1, n + 1):
    f = 1
    for j in range(1, i + 1):
        f *= j
    term = (x**(i-1))/f
    print(term, end = ' ')
    sun += term
print('\nsum =', sun)
print('\n')

#s = 1 + x/2 + x^2/3…
total = 0
for i in range(1, n + 1):
    total = total + ((x**(i-1))/i)
    print(((x**(i-1))/i), end = ' ')
print('\nsum =', total)
print('\n')

#s = x – x^2/2! + x^3/3! – x^4/4!
s = 0
for i in range (1,n+1):
    f=1
    for j in range(1,i+1):
        f=f*j
    t = (((-1)**(i-1)) * (x**i))/f
    print(t, end = ' ')
    s += t
print('\nsum =', s)




