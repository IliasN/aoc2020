def parse_txt(filename):
    with open(filename, "r") as f:
        lines = [line for line in f if line != "\n"]
    bags = dict()
    for line in lines:
        bag = dict()
        name = line.split("bags")[0].strip()
        if "no" not in line:
            rules = line.split("contain")[1].strip().replace("bags" , "").replace("bag", "").replace(".","").split(",")
            rules = [rule.strip().split(" ", 1) for rule in rules]
            rules = {rule[1]: int(rule[0]) for rule in rules}
        else:
            rules = {}
        bags[name] = rules
    return bags

# source = ou je cherche
# target = ce que je cherche
def can_hold(bags, source_key, target_key):
    if len(bags[source_key]) == 0:
        return False
    elif target_key in bags[source_key]:
        return True
    else:
        for key in bags[source_key]:
            res = can_hold(bags, key, target_key)
            if res:
                return res
        return False

def count_bags(bags, key):
    nb_bags = sum(list(bags[key].values()))
    for new_key in bags[key]:
        nb_bags += count_bags(bags, new_key) * bags[key][new_key]
    return nb_bags

bags = parse_txt("data")
count1 = 0
for key in bags:
    if can_hold(bags, key, "shiny gold"):
        count1 += 1
print("Part 1 :")
print(count1)

part2 = count_bags(bags, "shiny gold")
print("Part 2 :")
print(part2)
