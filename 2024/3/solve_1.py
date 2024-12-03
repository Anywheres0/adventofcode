import re

with open('input.txt') as inp:
    data = inp.read()

correct = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)

total = 0

for pair in correct:
    total += int(pair[0]) * int(pair[1])

print(total)
