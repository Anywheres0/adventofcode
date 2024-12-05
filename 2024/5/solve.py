
with open('input.txt') as inp:
    data = inp.read()

### Part 1
rules, orders = data.split("\n\n")

rules = rules.strip().splitlines()
orders = orders.strip().splitlines()

rules.sort()

after_defs = {}

for rule in rules:
    key = int(rule.split('|')[0])
    val = int(rule.split('|')[1])
    if key not in after_defs:
        after_defs[key] = []
    after_defs[key].append(val)

all_orders = [eval('[' + line + ']') for line in orders]

right_order = []
for order in all_orders:
    correct = True
    for idx, elem in enumerate(order[:-1]):
        after_current = order[idx+1:]
        if not all(num in after_defs[elem] for num in after_current):
            correct = False
            break
    if correct:
        right_order.append(order)
        
print(sum([i[len(i)//2] for i in right_order]))

### Part 2

wrong_orders = [i for i in all_orders if i not in right_order]
fixed_order = []

for w_order in wrong_orders:
    sorted_vers = [0 for _ in range(len(w_order))]
    for num in w_order:
        back = len(set(w_order) & set(after_defs[num])) #number of elements ahead of number that are in the list
        sorted_vers[len(w_order) - back - 1] = num
    fixed_order.append(sorted_vers)

print(sum([i[len(i)//2] for i in fixed_order]))
