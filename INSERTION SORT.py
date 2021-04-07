#  INSERTION SORT

lst=[]
n=int(input("Enter no of elements in list: "))
for i in range(0,n):
  x=input("Input element: ")
  lst.append(int(x))
for i in range(1,n):
  key=lst[i]
  j=i-1
  while j>=0 and lst[j]>key:
    lst[j+1]=lst[j]
    j-=1
  lst[j+1]=key
print(lst)
