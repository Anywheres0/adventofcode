
with open('input.txt') as inp:
    data = inp.read()

tests = []
for line in data.splitlines():
    calibration, nums = int(line.split(": ")[0]), [int(x) for x in line.split(": ")[1].split(" ")]
    tests.append([calibration, nums])

def test_possible(value, num_list, concat=False):
    #base case, single number in list
    if len(num_list) == 1:
        return value == num_list[0]
    #test if multiplication would work
    if (value / num_list[-1]) % 1 == 0 and test_possible(value // num_list[-1], num_list[:-1], concat):
        return True
    #test if concatenation would work
    if concat:
        #if the last elem in list is at the end of value and is not the same as value (if they're the same it runs out of chars)
        if str(num_list[-1]) == str(value)[-len(str(num_list[-1])):] and value != num_list[-1] and test_possible(int(str(value)[:-len(str(num_list[-1]))]), num_list[:-1], concat):
            return True

    #last opportunity, test addition
    return value - num_list[-1] >= 0 and test_possible(value - num_list[-1], num_list[:-1], concat)

no_concat_total = 0
concat_total = 0

for test in tests:
    no_concat_total += test_possible(test[0], test[1]) * test[0]
    concat_total += test_possible(test[0], test[1], concat=True) * test[0]

print(no_concat_total)
print(concat_total)
