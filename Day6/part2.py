with open("data", "r") as f:
    text = f.read()[0:-1]
groups_data = [g.split("\n") for g in text.split("\n\n")]

g_sets = []
for g_data in groups_data:
    tmp_sets = []
    for line in g_data:
        tmp = set()
        for c in line:
            tmp.add(c)
        tmp_sets.append(tmp)
    g_sets.append(tmp_sets[0].intersection(*tmp_sets))
print("Part 2 :")
print(sum([len(x) for x in g_sets]))
