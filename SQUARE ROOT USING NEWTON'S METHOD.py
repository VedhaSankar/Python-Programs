#    SQUARE ROOT USING NEWTON'S METHOD

n=int(input("Enter number: "))
a=0.5*n
b=0.5*(a+n/a)
while(b!=a):
  a=b
  b=0.5*(a+n/a)
print(a)
