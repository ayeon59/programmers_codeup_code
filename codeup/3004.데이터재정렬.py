n = int(input())
a=list(map(int,input().split()))

b = sorted(a)
arr=[]

for i in range(n):
    arr.append((b[i],i))

arr_d = dict(arr)
for i in a:
    print(arr_d[i], end=" ")



