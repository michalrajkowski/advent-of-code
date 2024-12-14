height_map : dict[tuple[int, int] : int]= {}

data_lines : list[str] = []
with open("data.txt") as file:
    data_lines = file.readlines()
    for j, line in enumerate(data_lines):
        for i, char in enumerate(line.strip()):
            height_map[(i,j)] = int(char)

MAX_J = len(data_lines)
MAX_I = len(data_lines[0].strip())
def is_in_map(point):
    if 0 <= point[0] < MAX_I and 0 <= point[1] < MAX_J:
        return True
    return False

trailheads_sum = 0
neighbour_modifier = [(-1,0),(1,0),(0,1),(0,-1)]

for point in height_map.keys():
    if height_map[point] != 0:
        continue
    visited_map = {p : False for p in height_map.keys()}
    queue : list = []
    visited_map[point] = True
    queue.append(point)
    while not (len(queue) == 0):
        this_point = queue.pop(0)
        if height_map[this_point] == 9:
            trailheads_sum+=1
        for mod in neighbour_modifier:
            new_point = (mod[0]+this_point[0], mod[1]+this_point[1])
            if not is_in_map(new_point):
                continue
            if visited_map[new_point]:
                continue
            if height_map[new_point] != height_map[this_point] + 1:
                continue
            visited_map[new_point] = True
            queue.append(new_point)

print(trailheads_sum)      