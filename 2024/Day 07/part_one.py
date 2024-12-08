import re
from itertools import product
import time


def is_equation_solvable(target_sum, numbers):
    operator_combinations = product("+*", repeat=len(numbers) - 1)

    for operators in operator_combinations:
        result = numbers[0]

        for num, operator in zip(numbers[1:], operators):
            if operator == "+":
                result += num
            elif operator == "*":
                result *= num
            
        if result == target_sum:
            return True 
    
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