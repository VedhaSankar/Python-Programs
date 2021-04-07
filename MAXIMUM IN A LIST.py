#   MAXIMUM IN A LIST

lst=[]
n=int(input("Enter no of elements in list: "))
for i in range(0,n):
  x=input("Input element: ")
  lst.append(int(x))
max=lst[0]
for i in range(0,n):
  if(max<lst[i]):
    max=lst[i]
print(max)
