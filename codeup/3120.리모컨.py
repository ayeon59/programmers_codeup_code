a, b =map(int,input().split())
count = 0
button_up=[10,5,1]
button_down=[-1,-5,-10]

while a!=b:
    if(a<b):
        
        for i in range(3):
            degree = a + button_up[i]
            if(degree>b):
                continue
            a = degree
            count += 1
            break
            print(a)
    else:
        
        for i in range(3):
            degree = a + button_down[i]
            if(degree>b):
                continue
            a = degree
            count += 1
            break

print(count)


#문제는 풀렸는데 시간초과 