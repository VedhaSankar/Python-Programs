#  SELECTION SORT

lst=[]
n=int(input("Enter no of elements in list: "))
for i in range(0,n):
  x=input("Input element: ")
  lst.append(int(x))
for i in range(0,n):
  s=i
  for j in range(i,n):
    if lst[j]<lst[s]:
      lst[j],lst[s]=lst[s],lst[j] 
print(lst)
