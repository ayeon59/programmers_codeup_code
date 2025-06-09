n,m = map(int,input().split())
x, y, direction=map(int,input().split())
place = [list(map(int, input().split())) for _ in range(n)]

steps=[(-1,0),(0,1),(1,0),(0,-1)]

def turn_left():
    global direction 
    direction -= 1
    if(direction==-1):
        direction = 3

count = 1
back_count = 0
while True:
    turn_left()
    if(back_count==4):
        nx = x + steps[(direction + 2) % 4][0]
        ny = y + steps[(direction + 2) % 4][1]

        if(place[nx][ny]==1):
            break
        else:
            x = nx
            y = ny 
        back_count = 0
    next_x = x+steps[direction][0]
    next_y = y+steps[direction][1]

    if(place[next_x][next_y]==1):
        back_count += 1
        continue

    else:
        place[next_x][next_y]=1
        back_count = 0
        count+=1
        turn_left()
        x = next_x
        y = next_y
print(count)