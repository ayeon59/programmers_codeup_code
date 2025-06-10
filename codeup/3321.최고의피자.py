n = int(input())
a,b = map(int,input().split())
c = int(input())
topping=[]
result = c/a
for i in range(n):
    topping.append(int(input()))

topping.sort(reverse=True)

for i in range(1,n):
    sum = c
    for j in range(i):
        sum += topping[j]
    calorie = sum / (a+(i*b))
    if(calorie>result):
        result = calorie
        print(result)

print(int(result))




