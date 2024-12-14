garden_map : dict[tuple[int , int] : int ] = {}
visited_field : dict[tuple[int , int] : bool ] = {}
area_field : dict[tuple[int , int] : int ] = {}
data_lines : list[str] = []

with open("data.txt") as file:
    data_lines = file.readlines()
    for j, line in enumerate(data_lines):
        for i, char in enumerate(line.strip()):
            garden_map[(i,j)] = ord(char)

MAX_J = len(data_lines)
MAX_I = len(data_lines[0].strip())
def is_in_map(point):
    if 0 <= point[0] < MAX_I and 0 <= point[1] < MAX_J:
        return True
    return False

visited_field = {key : False for key in garden_map.keys()}
area_field = {key : 0 for key in garden_map.keys()}
neighbour_modifiers = [(-1,0),(1,0),(0,-1),(0,1)]

for point in garden_map.keys():
    if visited_field[point]:
        continue
    perimiter_cache_list = []
    total_area = 0
    # Find all fields in this garden plant type. 
    # mark them as visited
    # calculate the area + perimiter
    queue = []
    queue.append(point)
    visited_field[point] = True

    while len(queue) > 0:
        this_point = queue.pop(0)

        perimiter_cache_list.append(this_point)
        total_area += 1
        
        for this_mod in neighbour_modifiers:
            next_point = (this_point[0]+this_mod[0],this_point[1]+this_mod[1])
            if not is_in_map(next_point):
                continue
            if visited_field[next_point]:
                continue
            if garden_map[next_point] != garden_map[this_point]:
                continue

            visited_field[next_point] = True
            queue.append(next_point)
    
    for cache_point in perimiter_cache_list:
        area_field[cache_point] = len(perimiter_cache_list)
    
# calculate perimiters / fences:
total_fence_cost = 0
for this_point in garden_map.keys():
    for this_mod in neighbour_modifiers:
        next_point = (this_point[0]+this_mod[0],this_point[1]+this_mod[1])
        # out of map border
        if not is_in_map(next_point):
            total_fence_cost+=area_field[this_point]
            continue

        if garden_map[this_point] != garden_map[next_point]:
            total_fence_cost+=area_field[this_point]
            continue

print(total_fence_cost)