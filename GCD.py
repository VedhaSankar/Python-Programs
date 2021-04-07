#   GCD OF TWO NUMBERS
 
d1 = int(input("Enter first number: "))
d2 = int(input("Enter second number: "))
rem=d1%d2
while rem!=0:
    d1=d2
    d2=rem
    rem=d1%d2
print('GCD of given numbers is: ',d2)
