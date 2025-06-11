n, m = map(int, input().split())
rice_cake = list(map(int, input().split()))

length = 0  # 결과 저장용

def cut_rice(array, cut, target):
    total = 0
    for x in array:
        if x > cut:
            total += x - cut
    return total >= target

def divide_rice(array, target, start, end):
    global length
    if start > end:
        return
    mid = (start + end) // 2
    if cut_rice(array, mid, target):
        length = mid  # 조건을 만족하면 일단 저장
        divide_rice(array, target, mid + 1, end)
    else:
        divide_rice(array, target, start, mid - 1)

divide_rice(rice_cake, m, 0, max(rice_cake))
print(length)
