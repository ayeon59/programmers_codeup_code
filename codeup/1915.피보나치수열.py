n = int(input())

def recall_fibonacci(number):
    if number <=2 :
        return 1
    return recall_fibonacci(number-1) + recall_fibonacci(number-2)

print(recall_fibonacci(n))