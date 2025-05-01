def DFS(L, total):
    global cnt
    if L == len(numbers):  # ✅ 유연하게 수정
        if total == target:
            cnt += 1
    else:
        DFS(L + 1, total + numbers[L])
        DFS(L + 1, total - numbers[L])


cnt = 0
numbers=[1,1,1,1,1]
target = 3
DFS(0,0)

print(cnt)