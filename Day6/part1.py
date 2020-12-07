with open("data", "r") as f:
    text = f.read()
groups_data = [g.replace("\n", "") for g in text.split("\n\n")]

g_sets = [0] * len(groups_data)
for i,g_data in enumerate(groups_data):
    g_sets[i] = set()
    for c in g_data:
        g_sets[i].add(c)
print("Part 1 :")
print(sum([len(x) for x in g_sets]))
