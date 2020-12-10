def parse(filename):
    with open(filename, "r") as f:
        adapters = [int(x) for x in f if x != "\n"]
    return sorted(adapters)

def compute_diffs(arr):
    diff = [0,1] # diff 3 starts at 1 because of our device
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
    ret = []
    current = arr[i]
    for x in arr[i+1:]:
        if x - current <= 3:
            ret.append(x)
        else:
            break
    return len(ret)


print("Part 1 :")
adapters = parse("data")
print(compute_diffs(adapters))

adapters.append(adapters[-1] + 3)
adapters.append(0)
adapters = sorted(adapters)
test = all_arranges(adapters)

print(test)
