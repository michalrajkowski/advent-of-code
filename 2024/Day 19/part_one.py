import re

towel_patterns = []
desings_list = []

with open("data.txt") as file:
    data_lines = file.readlines()
    for i, line in enumerate(data_lines):
        if i == 0:
            x = line.strip().split(", ")
            towel_patterns = x
            # Extract all tower pattens
        if i > 1:
            # append the designs
            desings_list.append(line.strip())
            pass

# Branch and bound
# Build random arrays of len and bound them if they are not possible?
found_count = 0
for i, design in enumerate(desings_list):
    top_len = 0
    # Check if building this pattern is possible:
    was_here_already = {}
    combinations = [""]
    print(i)
    while len(combinations) > 0:
        this_str = combinations.pop(0)
        if len(this_str) > len(design):
            continue
        if this_str == design:
            # We found it
            found_count+=1
            break
        if design.startswith(this_str):
            for pattern in towel_patterns:
                new_pattern = this_str+pattern
                if new_pattern in was_here_already.keys():
                    continue
                was_here_already[new_pattern] = True
                combinations.append(new_pattern)
print(found_count)