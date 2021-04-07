#  BINARY SEARCH 

lst=[]
n=int(input("Enter no of elements in list: "))
for i in range(0,n):
  x=input("Input element: ")
  lst.append(int(x))
e=int(input("Enter the element to be searched: "))
found = False
first = 0
last= n-1
while (first<=last and not found):
  mid=((first+last)//2)
  if (e==lst[mid]):
    found=True
  elif lst[mid]<e:
    first=mid+1
  elif lst[mid]>e:
    last=mid-1
if found:
  print(e," was found at index: ",mid)
else:
  print(e,"was not found.")
