n = int(input())
step = []

d=[0]*100000

for i in range(n):
    step.append(int(input()))

step.reverse()
count = 0
d[0]=step[0]
d[1]=max(step[1],step[2])
if d[1] == step[1] :
    count = 1 

for i in range(2,n+1):
    if count == 1 :
        count = 0
        continue
    d[i] = max(d[i-2]+step[i],d[i-1])
    if d[i] == d[i-1] :
        count = 1

print(d[n-1])

