import sys
sys.setrecursionlimit(10**6)

n=int(input())

def recall_sum(number):
    if number == 0 :
        return 0
    return number + recall_sum(number-1)

print(recall_sum(n))