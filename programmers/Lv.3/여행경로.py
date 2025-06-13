from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
  
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)
    
    path = []                       # 최종 경로를 담을 스택
    
    def dfs(airport):
        while graph[airport]:       # 갈 곳이 남아 있는 동안
            dfs(graph[airport].pop())
        path.append(airport)        # 막다른 길에서 push
    
    dfs("ICN")
    return path[::-1]               # 뒤집어서 리턴
