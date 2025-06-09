input_data=input()
row = int(input_data[1])
column = (ord(input_data[0]))-(ord('a')) + 1

x,y=row,column
count=0

dx=[2,2,-2,-2,1,-1,1,-1]
dy=[1,-1,1,-1,2,2,-2,-2]

for i in range(8):
    nx=x+dx[i]
    ny=y+dy[i]
    if(nx>8 or ny>8 or nx<1 or ny<1) :
        continue
    count += 1
print(count)
