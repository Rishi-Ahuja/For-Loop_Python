#Q11: WAP to print the following pattern:-

n = int(input('enter the no of rows: '))

'''
1
12
123
12345
'''
print('\npattern 1')
for x in range(1, n+1):
    for y in range(1, x+1):
        print(y, end = "")
    print()
    
'''
 12345
 1234
 123
 12
 1
 '''
print('\npattern 2')
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end='')
    print()
        
'''
55555
55555
55555
'''
print('\npattern 3')
for x in range(0, 3):
    for y in range(0, n):
        print(n, end = '')
    print()

'''
*
**
***
****
*****
'''
print('\npattern 4')
for x in range(1, n+1):
    for y in range(1, x+1):
        print('*', end = '')
    print()


'''
1
22
333
4444
55555
'''
print('\npattern 5')
for x in range(1, n+1):
    for y in range(1, x+1):
        print(x, end = '')
    print()