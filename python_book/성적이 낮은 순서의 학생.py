n = int(input())
a=[]
for i in range(n):
    input_data = input().split()
    a.append((input_data[0],int(input_data[1])))

a = sorted(a,key=lambda student:student[1])

for x in a:
    print(x[0],end=' ')