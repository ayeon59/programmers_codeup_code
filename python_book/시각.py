n = int(input())
count = 60*60*(n+1)
for i in range(n+1):
    if(i//10!=3 and i%10!=3):
        for j in range(60):
            if(j//10!=3 and j%10!=3):
                for k in range(60):
                    if(k//10!=3 and k%10!=3):
                        count -= 1
            

print(count)