n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

result = -99999

for i in range(n):  
    row_min = min(array[i]) 
    result = max(result, row_min) 

print(result)


#동일