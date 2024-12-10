from itertools import permutations

with open('input.txt') as inp:
    data = inp.read()

def get_indices(string, substr):
    indices = []
    start = 0
    while True:
        start = string.find(substr, start)
        if start == -1:
            break
        indices.append(start)
        start += 1
    return indices

unique_chars = set(list(data.replace("\n","").replace(".","")))
rows = data.splitlines()

unique_projs_p1 = []
unique_projs_p2 = []

for char in unique_chars:
    pos_linear = get_indices(data.replace("\n", ""), char)
    pos_rectangular = [[i // len(rows[0]), i % len(rows[0])] for i in pos_linear]
    perms = list(permutations(pos_rectangular, 2))
    for pair in perms:
        for i in range(len(rows[0])):
            proj = [pair[0][0] + i * (pair[0][0] - pair[1][0]), pair[0][1] + i * (pair[0][1] - pair[1][1])]
            if proj[0] >= 0 and proj[0] <= len(rows) - 1 and proj[1] >= 0 and proj[1] <= len(rows[0]) - 1:
                if proj not in unique_projs_p2:
                    unique_projs_p2.append(proj)
                if proj not in unique_projs_p1 and i == 1:
                    unique_projs_p1.append(proj)
            else:
                break
            
print(len(unique_projs_p1))
print(len(unique_projs_p2))
