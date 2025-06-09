h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) +str(j)+str(k):
                count += 1

print(count)

"""
시/분/초 를 문자로 변환 후 문자열에 '3'이 포함되어 있는 경우를 직접 카운트
"""