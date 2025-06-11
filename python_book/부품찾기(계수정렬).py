n = int(input())
array = [0] * 1000000

for i in input().split():
    array[int(i)] += 1

m = int(input())
customer = list(map(int,input().split()))

for i in customer :
    if array[i] == 1:
        print('yes', end=' ')
    else :
        print('no', end=' ')

