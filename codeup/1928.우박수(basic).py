n = int(input())

def recall_rain(number):
    if number == 1 :
        return 
    elif number % 2 == 0 :
        num = number // 2
        recall_rain(number // 2)
        print(num)
        return num
    else :
        num = (3*number)+1
        recall_rain((3*number)+1)
        print(num)
        return num
print(n)
recall_rain(n)