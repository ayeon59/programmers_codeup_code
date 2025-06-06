n, m, k = map(int, input().split())
a = list(map(int, input().split()))
count = 0
total=0

a.sort(reverse='True')
while(m>0):
    count = 0
    for i in range(k):
        total += a[0]
        m -= 1
    total += a[1]
    m -= 1

print(total)

