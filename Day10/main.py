import functools

def parse(filename):
    with open(filename, "r") as f:
        adapters = sorted([int(x) for x in f if x != "\n"])
    adapters.append(adapters[-1] + 3)
    adapters.append(0)
    return sorted(adapters)

def compute_diffs(arr):
    diff = [0,0] 
    last = 0
    for ad in arr:
        d = ad - last
        if d == 1:
            diff[0] += 1
        elif d == 3:
            diff[1] += 1
        last = ad
    return diff[0] * diff[1]


# Couldn't do it alone had to get help
def all_arranges(arr):
    count_array = [0] * len(arr)
    count_array[0] = 1
    for i,x in enumerate(arr):
        for j in range(valids_next(arr, i)):
            count_array[i+1+j] += count_array[i]
    return count_array[-1]


def valids_next(arr, i):
    ret = 0
    current = arr[i]
    for x in arr[i+1:]:
        if x - current <= 3:
            ret += 1
        else:
            break
    return ret

# python 3.9 utiliser @functools.cache
@functools.lru_cache(maxsize=None)
def recursive_solve(i):
    if i == len(arr)-1:
        return 1
    res = 0
    for j in range(1,4):
        if i+j < len(arr) and arr[i+j] - arr[i] <= 3:
            res += recursive_solve(i+j)
    return res


print("Part 1 :")
adapters = parse("data")
arr = adapters
print(compute_diffs(adapters))
print("Part 2 :")
part2 = all_arranges(adapters)
print(part2)
part2rec = recursive_solve(0)
print(part2rec)
assert part2 == part2rec
print("Recursive and linear are equal")
