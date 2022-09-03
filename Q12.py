#Q12: WAP to print hcf and lcm of any two numbers.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
 
hcf = 1
 
for i in range(2, a+1):
    if(a % i ==0 and b % i == 0):
        hcf = i
        
lcm = (a*b)//hcf

print("HCF of the numbers is: ", hcf)
print("LCM of the two numbers is: ", lcm)
