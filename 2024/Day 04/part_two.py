char_to_int_dict = {
        "." : -1,
        "X" : 0,
        "M" : 1,
        "A" : 2,
        "S" : 3,
    }

def char_to_int(char : str) -> int:
    global char_to_int_dict
    return char_to_int_dict[char]

xmas_map : dict[tuple[int,int], int]  = {}
visited_map : dict[tuple[int,int], bool]  = {}
data_lines = None

with open("data.txt", "r+") as file1:
    data_lines = file1.readlines()
    for j, line in enumerate(data_lines):
        for i, char in enumerate(line.strip()):
            xmas_map[(i,j)] = char_to_int(char)
            visited_map[(i,j)] = False

xmas_count = 0

MAX_J = len(data_lines)
MAX_I = len(data_lines[0].strip())
MAX_XMAS_VALUE = 3

def point_in_map(this_point : tuple[int,int]) -> bool:
    if 0 <= this_point[0] < MAX_I and 0 <= this_point[1] < MAX_J:
        return True
    return False

sorted_neighbours_template = [char_to_int_dict["M"], char_to_int_dict["M"], char_to_int_dict["S"], char_to_int_dict["S"]]
sorted_neighbours_template.sort()
neighbor_array_moves = [(1,1),(-1,-1),(1,-1),(-1,1)]
for i in range(0, MAX_I):
    for j in range(0, MAX_J):
        if xmas_map[(i,j)] != char_to_int_dict["A"]:
            continue
        # try to fit x-mas
        all_neighbours_in_map = all(point_in_map((i + dx, j + dy)) for dx, dy in neighbor_array_moves)
        if not all_neighbours_in_map:
            continue
        nei_array = [xmas_map[(i + dx, j + dy)] for dx, dy in neighbor_array_moves]
        if nei_array[0] == nei_array[1]:
            continue
        nei_array.sort()
        if nei_array == sorted_neighbours_template:
            xmas_count+=1
print(xmas_count)

