import copy

def check_line(line, decresing : bool) -> bool:

    for i in range(1, len(line)):
        a = line[i-1]
        b = line[i]
        # check condition
        # two adjacent levels differ by at least one and at most three.
        if not(abs(a - b) >= 1 and abs(a-b) <= 3):
            return False
        # Check order increasing
        if (a <= b and not decresing):
            return False
        if (a >= b and decresing):
            return False

    return True

levels_list = []

with open("data.txt", "r+") as file1:
    data_str = file1.readlines()
    for line in data_str:
        str_list = line.split()
        int_list = [int(item) for item in str_list]
        levels_list.append(int_list)

# For each line check the conditions:
levels_correct = 0
for line in levels_list:
    found = False
    # check increasing
    # Brute check - check each combination with one number missing:
    for i in range(len(line)):
        new_line : list[int] = copy.deepcopy(line)
        new_line.pop(i)
        if check_line(new_line, False):
            levels_correct+=1
            found = True
            break

    if found:
        continue
    # check decreasing
    for i in range(len(line)):
        new_line : list[int] = copy.deepcopy(line)
        new_line.pop(i)
        if check_line(new_line, True):
            levels_correct+=1
            found = True
            break