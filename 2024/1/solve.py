with open('input.txt') as inp:
    data = inp.read()

col1 = [int(line.split("   ")[0]) for line in data.split("\n")]
col2 = [int(line.split("   ")[1]) for line in data.split("\n")]
col1.sort()
col2.sort()

diffs = [abs(col1[i] - col2[i]) for i in range(len(col1))]

print("Part 1 - Total Difference:")
print(sum(diffs))

score = 0
for num in col1:
    score += num * col2.count(num)

print("Part 2 - Similarity Score:")
print(score)
