n = int(input())
a=[]
for i in range(n):
    input_text=input().split()
    a.append((input_text[0],int(input_text[1])))

a = sorted(a,key=lambda x:x[1])

print(a[-3][0])
