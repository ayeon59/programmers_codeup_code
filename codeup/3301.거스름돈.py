n = int(input())
coin_types=[50000,10000,5000,1000,500,100,50,10]
count = 0

for x in coin_types:
    count += n//x
    n = n%x


print(count)