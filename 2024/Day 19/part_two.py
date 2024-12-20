import re
from queue import PriorityQueue

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
    mini_found_count = 0
    top_len = 0
    # Check if building this pattern is possible:
    was_here_already = {}
    pq = PriorityQueue()
    pq.put((0, ""))
    was_here_already[""] = 1
    while not pq.empty():
        (this_priority, this_str) = pq.get()
        if len(this_str) > len(design):
            continue
        if design.startswith(this_str):
            for pattern in towel_patterns:
                new_pattern = this_str+pattern
                if new_pattern in was_here_already.keys():
                    was_here_already[new_pattern]+=was_here_already[this_str]
                    continue
                else:
                    was_here_already[new_pattern]=was_here_already[this_str]
                pq.put((len(new_pattern), new_pattern))
    if design in was_here_already.keys():
        print(i,": ", was_here_already[design])
        found_count+=was_here_already[design]
    else:
        print(i,": ", "NOT FOUND")
print(found_count)