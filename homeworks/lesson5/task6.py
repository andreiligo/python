def sum_strnum(string):
    summary = []
    n_str = ''
    for s in string + '_':
        if s.isdigit():
            n_str += s
        elif n_str:
            summary.append(int(n_str))
            n_str = ''
        else:
            continue
    return sum(summary)

acad_subj = {}

with open("task6.txt", encoding="utf-8") as file:
    for string in file:
        subj = string[:string.index(':')]
        acad_subj[subj] = sum_strnum(string)

print(acad_subj)
