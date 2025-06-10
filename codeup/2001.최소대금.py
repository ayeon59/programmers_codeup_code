pasta = []
drink = []

for i in range(3):
    pasta.append(int(input()))

for i in range(2):
    drink.append(int(input()))

pasta.sort()
drink.sort()

total=pasta[0]+drink[0]
print(total)
total += total * 0.1
print(total)