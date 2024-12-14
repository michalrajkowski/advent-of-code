import re
from sympy import symbols, Eq, solve
GIANT_CONSTANT = 10000000000000
pattern_button = r'X\+(\d+), Y\+(\d+)'
pattern_result = r'X\=(\d+), Y\=(\d+)'
problems = []
with open("data.txt") as file:
    data_lines = file.readlines()
    i = 0
    while i < len(data_lines):
        # Extract button A numbers:
        match = re.search(pattern_button, data_lines[i])
        x1 = int(match.group(1))
        y1 = int(match.group(2))
        i+=1
        # Extract button B numbers:
        match = re.search(pattern_button, data_lines[i])
        x2 = int(match.group(1))
        y2 = int(match.group(2))
        i+=1
        # Extract equation result:
        match = re.search(pattern_result, data_lines[i])
        x3 = int(match.group(1))
        y3 = int(match.group(2))
        x3+=10000000000000
        y3+=10000000000000
        i+=2
        problems.append((x1,y1,x2,y2,x3,y3))

tokens_spent = 0
for problem in problems:
    # Define variables
    (x1,y1,x2,y2,x3,y3) = problem
    A, B = symbols('A B')
    # Create equations dynamically
    eq1 = Eq(x1 * A + x2 * B, x3)  # Coefficients for X
    eq2 = Eq(y1 * A + y2 * B, y3)  # Coefficients for Y

    # Solve the equations
    solution = solve((eq1, eq2), (A, B))
    print(solution)
    res_a, res_b = solution[A], solution[B]
    if (res_a.is_integer and res_b.is_integer):
        tokens_spent+= res_a*3 + res_b

print(tokens_spent)