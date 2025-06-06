n,m,k = map(int,input().split())
data = list(map(int,input().split()))
total = 0

data.sort()
first=data[n-1]
second=data[n-2]

count = int(m/(k+1))*k
count += m % (k+1)

total += first*count
total += second*(m-count)

print(total)

"""
반복문을 사용하지 않고 수학적으로 계산하기 때문에
값을 계산하기 위해 반복할 필요가 없어 시간복잡도가 줄어든다.

당장 큰 값을 최대한 더하는 것이 최적의 해를 내므로 그리디 알고리즘으로 풀이할 수 있다.
"""