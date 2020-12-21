def parse(filename):
    ret = list()
    alerset = set()
    with open(filename, "r") as f:
        lines = [ line.replace("\n", "")  for line in f ]
    for line in lines:
        ingredients = line.split("(")[0].strip().split()
        alergenes = [x.strip() for x in  line.split("(")[1].replace("contains", "").replace(")", "").strip().split(",")]
        for i in alergenes:
            alerset.add(i)
        ret.append((ingredients, alergenes))
    return ret, alerset

def solve1(lines, alerset):
    lines_cpy = lines.copy()
    alergenes_found = dict()
    cnt = True
    ret_set = set()
    while len(alerset) != 0 and cnt:
        cnt = False
        for aler in alerset:
            curr_sets = list()
            for line in lines:
                found_set = set()
                if aler in line[1]:
                    for ingr in line[0]:
                        found_set.add(ingr)
                    curr_sets.append(found_set)
            if len(curr_sets) > 0:
                result_set = curr_sets[0].intersection(*curr_sets)
                if len(result_set) == 1:
                    cnt = True
                    ingr = list(result_set)[0]
                    alerset.remove(aler)
                    ret_set.add(ingr)
                    alergenes_found[ingr] = aler
                    for line in lines:
                        if ingr in line[0]:
                            line[0].remove(ingr)
                        if aler in line[1]:
                            line[1].remove(aler)
                    break
    count = 0
    for line in lines_cpy:
        for i in line[0]:
            if i not in ret_set:
                count += 1
    return count, alergenes_found

lines, alerset = parse("data")
res1, part2 = solve1(lines.copy(), alerset.copy())
print(res1)

res2 = ",".join(sorted(part2, key=lambda x : part2[x]))
print(res2)
