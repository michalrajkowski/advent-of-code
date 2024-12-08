anti_nodes : dict[tuple[int,int] : bool]= {}
antena_dicts : dict[str : list[tuple[int,int]]] = {}

with open("data.txt") as file:
    data_lines = file.readlines()
    for j, line in enumerate(data_lines):
        for i, char in enumerate(line.strip()):
            if char == ".":
                continue
            if not (char in antena_dicts.keys()):
                antena_dicts[char] = []
            antena_dicts[char].append((i,j))

MAX_J = len(data_lines)
MAX_I = len(data_lines[0].strip())

def point_in_map(this_point : tuple[int,int]) -> bool:
    if 0 <= this_point[0] < MAX_I and 0 <= this_point[1] < MAX_J:
        return True
    return False

def calculate_point_three(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    x3 = x2 + (x2 - x1)
    y3 = y2 + (y2 - y1)

    return (x3, y3)

for antena_list in antena_dicts.values():
    for first_antena_point in antena_list:
        for second_antena_point in antena_list:
            if first_antena_point == second_antena_point:
                continue
            antinode_point = calculate_point_three(first_antena_point, second_antena_point)
            if point_in_map(antinode_point):
                anti_nodes[antinode_point] = True

total_sum = 0
for val in anti_nodes.values():
    if val:
        total_sum+=1
print(total_sum)