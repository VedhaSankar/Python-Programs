#  MERGE SORT
 
def mergesort(arr):
  if len(arr)>1:
    mid=len(arr)//2
    L=arr[:mid]
    R=arr[mid:]
    mergesort(L)
    mergesort(R)
    i=j=k=0
    while i<len(L) and j<len(R):
      if L[i]<R[j]:
        arr[k]=L[i]
        i+=1
      else:
        arr[k]=R[j]
        j+=1
      k+=1
    while i<len(L):
      arr[k]=L[i]
      k+=1
      i+=1
    while j<len(R):
      arr[k]=R[j]
      k+=1
      j+=1
arr=[]
n=int(input("Enter the number of elememts in the list: "))
for i in range (0,n):
  x=int(input("Enter elememt: "))
  arr.append(x)
mergesort(arr)
for i in range (0,n):
  print(arr[i],end=' ')
