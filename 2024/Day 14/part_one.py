import re

pattern = r'-?\d+'
guard_data : list[tuple[int,int,int,int]]= []
# Get the input data
with open("data.txt") as file:
    data_lines = file.readlines()
    for line in data_lines:
        matches = re.findall(pattern, line)
        matches_int = [int(x) for x in matches]
        guard_data.append(tuple(matches_int))

MAP_X, MAP_Y = 101, 103
NUM_OF_SEC = 100
final_guards_pos = []
# Calculate each guard final place:
for guard_params in guard_data:
    (x,y,v_x,v_y) = guard_params
    final_x = (x+v_x*NUM_OF_SEC)%MAP_X
    final_y = (y+v_y*NUM_OF_SEC)%MAP_Y
    final_guards_pos.append((final_x, final_y))

# Calculate the safety quadrants values
quadrant_counts = [0 for i in range(4)]
for final_pos in final_guards_pos:
    (x,y) = final_pos
    half_x = MAP_X // 2
    half_y = MAP_Y // 2

    # Exclude boundaries
    if x == half_x or y == half_y:
        continue

    # Determine the quadrant
    if x > half_x and y > half_y:
        quadrant_counts[0] += 1  # Q1
    elif x < half_x and y > half_y:
        quadrant_counts[1] += 1  # Q2
    elif x < half_x and y < half_y:
        quadrant_counts[2] += 1  # Q3
    elif x > half_x and y < half_y:
        quadrant_counts[3] += 1  # Q4
print(quadrant_counts)
result = 1
for q in quadrant_counts:
    result*=q
print(result)