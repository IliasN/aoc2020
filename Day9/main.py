def parse_data(filename):
    with open(filename, "r") as f:
        lines = [int(x) for x in f if x != "\n"]
    return lines

def analyse_array(arr):
    for i in range(25, len(arr)):
        if not contains_sum(arr[i-25:i], arr[i]):
            print(arr[i])
            return arr[i]
    return -1


def contains_sum(arr, n):
    arr_set = set(arr)
    for x in arr_set:
        if (n - x) in arr_set:
            return True
    return False

def search_sum(arr, n):
    acc = 0
    start_index = 0
    i = 0
    while i < len(arr):
        x = arr[i]
        if x != n:
            acc += x
            if acc > n:
                acc = 0
                i = start_index
                start_index = i + 1
            if acc == n:
                weak = min(arr[start_index: i+1]) + max(arr[start_index: i+1])
                sum_n = i + 1 - start_index
                print(f"Part 2 :\nSolution found at index : i={start_index} encryption weakness : {weak} sum of {sum_n} terms")
        else:
            acc = 0
            i = start_index
            start_index = i + 1
        i += 1


data_arr = parse_data("data")
print("Part 1 :")
invalid = analyse_array(data_arr)

search_sum(data_arr, invalid)
