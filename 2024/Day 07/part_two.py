import re
from itertools import product
import time
from collections import deque

def is_equation_solvable(target_sum, numbers):
    operators_list = ["+", "*", "||"]
    remembered_results = {}
    queue = deque([[]])
    
    remembered_results[tuple([])] = numbers[0]

    while queue:
        this_operators = queue.popleft()
        if len(this_operators) == len(numbers) - 1:
            if remembered_results[tuple(this_operators)] == target_sum:
                return True  
            continue  

        for operator in operators_list:
            result = remembered_results[tuple(this_operators)]
            new_result = 0

            if operator == "+":
                new_result = result + numbers[len(this_operators)+1]
            elif operator == "*":
                new_result = result * numbers[len(this_operators)+1]
            elif operator == "||":
                new_result = int(str(result) + str(numbers[len(this_operators)+1]))
            
            if new_result <= target_sum:
                new_operators = tuple(this_operators) + (operator,)
                remembered_results[new_operators] = new_result
                
                queue.append(list(new_operators))
    
    return False

data_lines = []
with open("data.txt") as file:
    data_lines = file.readlines()

totalsum=0
tosolve_lines = []

start_time = time.time()

for line in data_lines:
    stripped_line = line.strip()
    if stripped_line == "":
        continue
    
    matches = re.findall(r'\d+', stripped_line)
    if matches:
        target_sum = int(matches[0])
        numbers = list(map(int, matches[1:]))
        
        solvable = is_equation_solvable(target_sum, numbers)
        tosolve_lines.append((target_sum, numbers, solvable))
        if solvable:
            totalsum+=target_sum
        
        # Print results for each line
        # print(f"Line: {stripped_line}")
        # print(f"Target Sum: {target_sum}, Numbers: {numbers}, Solvable: {solvable}")

print("--- %s seconds ---" % (time.time() - start_time))
print(totalsum)