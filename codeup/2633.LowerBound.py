n, k = map(int,input().split())
a = list(map(int,input().split()))
result = -1
def binary_number(array,target,start,end):
    global result
    if start > end:
        return
    mid = (start+end)//2
    if array[mid] >= target :
        result = mid
        binary_number(array,target,start,mid-1)
    else:
        binary_number(array,target,mid+1,end)
    

binary_number(a,k,0,n-1)

if result==-1 :
    print(n+1)
else :
    print(result+1)
