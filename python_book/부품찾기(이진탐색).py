n = int(input())
store = list(map(int,input().split()))
m = int(input())
customer = list(map(int,input().split()))

store.sort()

def binary_sort(array,target,start,end):
    if start > end :
        print("no")
        return 
    mid = (start+end)//2
    if array[mid] == target :
        print("yes")
        return
    elif array[mid] > target :
        return binary_sort(array,target,start,mid-1)
    else : 
        return binary_sort(array,target,mid+1,end)

for i in range(m):
    target = customer[i]
    binary_sort(store,target,0,n-1)

             