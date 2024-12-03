import re

with open('input.txt') as inp:
    data = inp.read()

data = "do()" + data

total = 0
while True:
    if "do()" in data:
        if "don't()" in data:
            dontafterdo = data[data.index("do()"):].index("don't()") + data.index("do()")
            tempslice = data[data.index("do()") : dontafterdo]
            data = data[dontafterdo + 7:]
        else:
            tempslice = data[data.index("do()"):]
            data = ""
        correct = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", tempslice)
        for pair in correct:
            total += int(pair[0]) * int(pair[1])
        
    else:
        print(total)
        break
