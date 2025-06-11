n = int(input())
store = set(map(int,input().split()))
m = int(input())
customer = list(map(int,input().split()))

for x in customer :
    if x in store :
        print('yes', end=' ')
    else :
        print('no', end=' ')