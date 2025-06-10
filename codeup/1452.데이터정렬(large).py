n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))

number = max(a)

arr = [0]*(number+1)

for i in range(n):
    arr[a[i]] += 1


for i in range(len(arr)):
    for j in range(arr[i]):
        print(i, end=" ")
