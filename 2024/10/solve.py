
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

def count_trails(grid, pos, rating=False):
    if rating:
        total = 0
    else:
        total = []
    neighbors = []
    if pos[0] + 1 < len(grid[0]) and grid[pos[0] + 1][pos[1]] == grid[pos[0]][pos[1]] + 1:
        neighbors.append([pos[0] + 1, pos[1]])
    if pos[0] - 1 >= 0 and grid[pos[0] - 1][pos[1]] == grid[pos[0]][pos[1]] + 1:
        neighbors.append([pos[0] - 1, pos[1]])
    if pos[1] + 1 < len(grid) and grid[pos[0]][pos[1] + 1] == grid[pos[0]][pos[1]] + 1:
        neighbors.append([pos[0], pos[1] + 1])
    if pos[1] - 1 >= 0 and grid[pos[0]][pos[1] - 1] == grid[pos[0]][pos[1]] + 1:
        neighbors.append([pos[0], pos[1] - 1])


    if grid[pos[0]][pos[1]] == 9:
        if rating:
            return 1
        else:
            return [pos]
    else:
        for neighbor in neighbors:
            if grid[neighbor[0]][neighbor[1]] == grid[pos[0]][pos[1]] + 1: 
                total += count_trails(grid, neighbor, rating)
    return total

def linearize_coords(inp_list):
    out = []
    for coord in inp_list:
        out.append(43 * coord[0] + coord[1])
    return out

field = [[int(x) for x in list(i)] for i in data.splitlines()]

total_score = 0
total_rating = 0

for idx in get_indices(data.replace("\n",""),"0"):
    total_score += len(set(linearize_coords(count_trails(field, [idx // len(field[0]), idx % len(field[0])]))))
    total_rating += count_trails(field, [idx // len(field[0]), idx % len(field[0])], rating=True)

print(total_score)
print(total_rating)

