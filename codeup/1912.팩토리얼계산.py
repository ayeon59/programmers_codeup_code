n = int(input())

def recall_factorial(number):
    if number == 1:
        return 1
    return number*recall_factorial(number-1)

print(recall_factorial(n))