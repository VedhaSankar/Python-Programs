#   FINDING THE POWER OF A NUMBER

x=int(input("Enter x: "))
y=int(input("Enter y: "))
p=x
if (y==0):
  p=1
else:
  while (y>1):
    p*=x
    y-=1
print(p)
