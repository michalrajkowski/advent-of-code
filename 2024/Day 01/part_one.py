list_1 = []
list_2 = []

with open("data.txt", "r+") as file1:
    data_str = file1.readlines()
    for line in data_str:
        (a,b) =map(int, line.split())
        list_1.append(a)
        list_2.append(b)

list_1.sort()
list_2.sort()

distance = 0

for i in range(len(list_1)):
    distance+=abs(list_1[i]-list_2[i])

print(distance)
