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

total_sum = 0

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

    # Find the number of edges:
    #   - indentify all of the border-points
    #   - group them?

    # Find all of the border points
    border_points = []
    for this_point in perimiter_cache_list:
        for this_mod in neighbour_modifiers:
            next_point = (this_point[0]+this_mod[0],this_point[1]+this_mod[1])
            if not is_in_map(next_point):
                border_points.append((this_point, next_point, this_mod))
                continue

            if garden_map[this_point] != garden_map[next_point]:
                border_points.append((this_point, next_point, this_mod))
                continue
    # Sort border points
    # so they are alligned top -> bottom and left -> right
    sorted_border_points = []
    for b_point in border_points:
        (p1,p2, direction) = b_point
        if p1[0] == p2[0]:
            # allign y
            if p1[1] > p2[1]:
                sorted_border_points.append(("v",p1,p2,direction))
            else:
                sorted_border_points.append(("v",p2,p1,direction))
        else:
            # allign x
            if p1[0] > p2[0]:
                sorted_border_points.append(("h",p1,p2,direction))
            else:
                sorted_border_points.append(("h",p2,p1,direction))
    # group those lines:
    # - take point
    # - as long as it is possibl to assign a point next to any in group, assign it,
    # - if no assigned during the iteration, it is the group
    
    edges_count = 0
    while len(sorted_border_points) > 0:
        this_border = sorted_border_points.pop(0)
        (vh_str,p1,p2,direction) = this_border
        # create new group
        this_group = []
        this_group.append(this_border)
        while True:
            found_element = None
            # try to find an element is 
            for next_border_point in sorted_border_points:
                # check if they are next to each other
                if next_border_point[0] != this_border[0]: # Check if horizontal/vertical match
                    continue
                if next_border_point[3] != this_border[3]:
                    continue
                # check if next_border_point is next to any point in this_group:
                # if vh_str == v -> y the same for both and x max difference is one
                for group_point in this_group:
                    if vh_str == "v":
                        if (group_point[1][1] == next_border_point[1][1]) and (abs(group_point[1][0] - next_border_point[1][0]) == 1):
                            # We found it!
                            found_element = next_border_point
                            break
                    else:
                        if (group_point[1][0] == next_border_point[1][0]) and (abs(group_point[1][1] - next_border_point[1][1]) == 1):
                            # We found it!
                            found_element = next_border_point
                            break
                if found_element != None:
                    break
            if found_element == None:
                edges_count+=1
                break
            # remove found element from all?
            if found_element in sorted_border_points:
                sorted_border_points.remove(found_element)
            this_group.append(found_element)
    total_sum+=edges_count*total_area
print(total_sum)