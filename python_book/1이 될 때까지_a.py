n,k = map(int,input().split())
result = 0

while True:
    target = (n//k)*k
    result += (n-target)
    n = target
    if(n<k):
        break
    result += 1
    n = n//k


result += (n-1)
print(result)

"""
n /= k 와 n//=k 는 자료형이 float과 int로 다름 유의
"""