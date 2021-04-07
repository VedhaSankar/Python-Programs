# LINEAR SEARCH using while loop
 
 
lst=[]
n=int(input("Enter no of elements in list: "))
for i in range(0,n):
  x=input("Input element: ")
  lst.append(int(x))
flag=0
e=int(input("Enter element to be searched: "))
i=0
while i<n:
    if(e==lst[i]):
     index=i
     flag=1
     break
    else:
      i+=1
if flag==1:
  print("Element found at index ",index)
else:
  print("Not found")
