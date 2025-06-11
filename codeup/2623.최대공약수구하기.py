arr = list(map(int, input().split()))
a = min(arr)
b = max(arr)
start = 0
end = a
answer = 1
while start<=end:
    mid = (start+end)//2
    if a % mid ==0 and b % mid == 0:
        answer = mid
        start = mid+1
    else :
        end = mid-1

print(answer)