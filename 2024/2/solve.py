with open('data.txt') as data_txt:
    data = data_txt.read()

reports = [[int(num) for num in line.split(" ")] for line in data.split("\n")]

def is_safe(report: list): 
    diffs = [elem - report[idx] for idx, elem in enumerate(report[1:])]
    try:
        if len(set([diff//abs(diff) for diff in diffs])) == 1:
            if (max(diffs) <= 3 and min(diffs) >= 1) or (min(diffs) >= -3 and max(diffs) <= -1):
                return True
    except:
        pass
    return False

def is_safe_without_one(inp_report: list):
    for i in range(len(inp_report)):
        report = inp_report.copy()
        report.pop(i)
        diffs = [elem - report[idx] for idx, elem in enumerate(report[1:])]
        try:
            if len(set([diff//abs(diff) for diff in diffs])) == 1:
                if (max(diffs) <= 3 and min(diffs) >= 1) or (min(diffs) >= -3 and max(diffs) <= -1):
                    return True
        except:
            pass
    return False

safe = 0
safe_wo_one = 0

for rep in reports:
    safe += is_safe(rep)
    safe_wo_one += is_safe_without_one(rep)

print(safe)
print(safe_wo_one)
