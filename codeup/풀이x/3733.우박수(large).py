a, b = map(int,input().split())
max_count = 0

d = [0]*1000000

def recall_rain(number,step):
    if number == 1 :
        return step
    if number % 2 == 0 :
        step += 1
        num = number // 2
        if d[num] != 0 :
            return d[num]
        
        d[num] = recall_rain(num,step) + 1
        return d[num]
    
    else :  
        step += 1  
        num = (3 * number) + 1
        if d[num] != 0 :
            return d[num]

        d[num] = recall_rain(num,step) + 1
        return d[num]
    

index = 0
index_result = 0

for i in range(a,b+1):
    result = recall_rain(i,0)
    if result and result > index_result :
        index = i
        index_result = result

print(index, index_result)


#메모리 문제 