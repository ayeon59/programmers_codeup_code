n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

for i in range(1,n):
    for j in range(i,0,-1):
        if a[j]<a[j-1] :
            a[j],a[j-1]=a[j-1],a[j]
        else : 
            break

for i in range(n):
    print(a[i])
