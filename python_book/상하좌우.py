n = int(input())
travel_x = 1
travel_y = 1

move = {
    'R': (0, 1),   
    'L': (0, -1), 
    'U': (-1, 0),  
    'D': (1, 0)   
}

commands = input().split()
for cmd in commands:
    dx, dy = move[cmd]
    if((travel_x+dx)>=1 and (travel_x+dx)<=n):
        travel_x += dx
    if((travel_y+dy)>=1 and (travel_y+dy)<=n):
        travel_y += dy
    print(travel_x,travel_y)

print(travel_x,travel_y)