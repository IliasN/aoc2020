input_data = list(map(int, "398254716"))
test_data = list(map(int, "389125467"))

class Node:
    def __init__(self, value):
        self.value = value
        self.n = None

    def print(self):
        print(self.value, end="")
        curr = self.n
        while curr != None and curr != self:
            print(curr.value, end="")
            curr = curr.n
        print()

    def __iter__(self):
        yield self.value
        curr = self.n
        while curr != None and curr != self:
            yield curr.value
            curr = curr.n

    def with_value(self, target):
        curr = self.n
        while curr.value != target and curr != None and curr != self:
            curr = curr.n
        return curr

def million(arr):
    arrc = arr.copy()
    value = max(arr) + 1
    while len(arrc) < 1000000:
        arrc.append(value)
        value += 1
    return arrc

def list_from_arr(arr):
    mydict = dict()
    root = Node(arr[0])
    curr = root
    mydict[curr.value] = curr
    for x in arr[1:]:
        curr.n = Node(x)
        curr = curr.n
        mydict[curr.value] = curr
    curr.n = root
    return root, mydict

def solve1(circ, mydict, n, mini, maxi):
    curr = circ
    for i in range(n):
        removed = curr.n
        curr.n = removed.n.n.n
        removed.n.n.n = None
        dest_value = curr.value - 1
        minic = mini.copy()
        maxic = maxi.copy()
        for x in removed:
            if x in minic:
                minic.remove(x)
            if x in maxic:
                maxic.remove(x)
        if dest_value < min(minic):
            dest_value = max(maxic)
        while dest_value in removed:
            dest_value -= 1
            if dest_value < min(minic):
                dest_value = max(maxic)
        dest_node = mydict[dest_value]
        removed.n.n.n = dest_node.n
        dest_node.n = removed
        curr = curr.n # laisser à la fin


newdata = million(input_data)
minimums = sorted(newdata)[:4]
maximums = sorted(newdata, reverse=True)[:4]
root, mydict = list_from_arr(newdata)
solve1(root, mydict, 10000000, minimums, maximums)
one = mydict[1]
v1 = one.n.value
v2 = one.n.n.value
print(f"{v1} * {v2} = {v1*v2}")
