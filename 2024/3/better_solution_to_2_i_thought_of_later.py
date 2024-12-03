import re

with open('input.txt') as inp:
    data = inp.read()

data = "do()" + data
data = data.replace("\n", "").replace("don't()","\n").replace("do()", "\n\n")

lines=data.splitlines() 
sum = 0 
for i, line in enumerate(lines ): 
    if  not lines[i-1]:
        correct = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line )
        for pair in correct:
            sum +=  int( pair[0]) * int(pair[1])

print(sum)
