start,end = map(int,input().split())

def print_odd(number,max):
    if number == max+1 :
        return 
    elif number%2==0 :
        print_odd(number+1,max)
    else :
        print(number,end=" ")
        print_odd(number+1,max)

print_odd(start,end)


