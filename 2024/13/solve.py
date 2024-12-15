import numpy as np
import re

with open('input.txt') as inp:
    data = inp.read()

machines = data.split("\n\n")

cost = 0

for machine in machines:
    lines = machine.splitlines()
    button_a_values = [int(x) for x in re.findall(r"\d+",lines[0])]
    button_b_values = [int(x) for x in re.findall(r"\d+",lines[1])]
    final_pos = np.array([int(x) for x in re.findall(r"\d+",lines[2])])
    coeffs = np.array(list(zip(button_a_values, button_b_values)))
    presses = np.linalg.solve(coeffs, final_pos)
    if all(np.isclose(num, round(num)) for num in presses) and all(num <= 100 and num >= 0 for num in presses):
        cost += 3 * round(presses[0])
        cost += round(presses[1])

print(cost)

### Part 2

cost = 0

for machine in machines:
    lines = machine.splitlines()
    button_a_values = [int(x) for x in re.findall(r"\d+",lines[0])]
    button_b_values = [int(x) for x in re.findall(r"\d+",lines[1])]
    final_pos = np.array([int(x) + 10000000000000 for x in re.findall(r"\d+",lines[2])])
    coeffs = np.array(list(zip(button_a_values, button_b_values)))
    presses = np.linalg.solve(coeffs, final_pos)
    if all(np.isclose(num, round(num), rtol=0, atol=1e-4) for num in presses) and all(num >= 0 for num in presses): #remove 100 constraint, specify absolute tolerance bcs at this scale it always returns true otherwise
        cost += 3 * round(presses[0])
        cost += round(presses[1])

print(cost)
