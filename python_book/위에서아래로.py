import time
start_time = time.time()

n = int(input())
array=[]


for i in range(n):
    array.append(int(input()))

array.sort()


for i in array:
    print(i, end=" ")

end_time=time.time()
print("time :",end_time-start_time)
