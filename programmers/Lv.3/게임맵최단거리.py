from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    
    q = deque()
    q.append((0,0))
    
    while q :
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx>=n or ny <= -1 or ny>=m :
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                q.append((nx,ny))
                maps[nx][ny] = maps[x][y] + 1
                
    result = maps[n-1][m-1]     
    if result == 1 :
        return -1
    else :
        return result
    
                
    