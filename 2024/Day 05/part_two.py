import copy
# Numbers in list can't be after number in key in instruction set
forbiden_after : dict[int, list[int]] = {key: [] for key in range(100)}
all_instruction_lists : list[list[int]]= []
with open("data.txt", "r+") as file1:
    is_first_imput_data_part : bool = True
    data_lines = file1.readlines()
    for line in data_lines:
        if line.strip() == "":
            # We found the empty line, switch mode to second
            is_first_imput_data_part = False
            continue
        if is_first_imput_data_part:
            # load condition line
            condition_numbers_str = line.strip().split("|")
            a, b = int(condition_numbers_str[0]), int(condition_numbers_str[1])
            forbiden_after[b].append(a)
            continue
        # load data lines
        instruction_list_str = line.strip().split(",")
        this_instruction_list = [int(x) for x in instruction_list_str if x.strip()]        
        all_instruction_lists.append(this_instruction_list)

middle_sum : int = 0


# Do the weird sort in case of failure -> insert the number in the first place after the rule is broken. Then proceed again from number in current index
remembered_list = None
for this_list in all_instruction_lists:
    print(this_list)
    is_correct_update = True
    remembered_list = copy.deepcopy(this_list)
    # go through all indexes from i to len
    for i in range(len(this_list)):
        while True:
            is_rule_broken = False
            x = remembered_list[i]
            # Try to go through all
            # if sth is not right we do the repair plan and try again.
            # If everything is fine, then we are gucci and exit true!!
            next_copy = copy.deepcopy(remembered_list)
            for j in range(i+1, len(remembered_list)):
                y = remembered_list[j]
                if not y in forbiden_after[x]:
                    continue
                # RULE HAS BEEN BROKEN!!!
                # set flag and insert the list element AFTER the broken one
                is_rule_broken = True
                is_correct_update = False
                next_copy.insert(j+1, x)
                next_copy.pop(i)
                break
            if not is_rule_broken:
                break
            remembered_list = copy.deepcopy(next_copy)
    # Add to score the middle element from list
    if not is_correct_update:
        middle_index = len(remembered_list) // 2
        middle_element = remembered_list[middle_index]
        middle_sum += middle_element
print(middle_sum)