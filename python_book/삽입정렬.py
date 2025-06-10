array=[7,5,4,3,2]

for i in range(1,len(array)):
    target=array[i]
    for j in range(0,i):
        if array[j]>target:
            array[j], array[i] = array[i],array[j]
            break
print(array)

