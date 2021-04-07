#   LINEAR SEARCH using for loop
 
 
lst=[]
n=int(input("Enter no of elements in list: "))
for i in range(0,n):
  x=input("Input element: ")
  lst.append(int(x))
flag=1
e=int(input("Enter element to be searched: "))
for i in range(0,n):
  if(flag==1):
    if(e==lst[i]):
     index=i
     flag=0
if flag==0:
  print("Element found at index ",index)
else:
  print("Not found")
