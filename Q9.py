#Q9: WAP to print  whether  the  number entered by the user is prime or not.

n = int(input('enter n: '))
flag = False

if n <= 1:
    print('num is neither prime nor composite')
else:
    for x in range(2, (n//2)+1):
        if n % x == 0:
            flag = True
            break
        else:
            pass

    if flag == False :
        print('num is prime')
    else:
        print('num is composite')