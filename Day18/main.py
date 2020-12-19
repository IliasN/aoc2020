def parse(filename: str) -> list:
    with open(filename, "r") as f:
        lines = [ line for line in f if line != "\n" or line != ""]
    return lines

def apply(op: str, a: int, b: int) -> int:
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a // b

# Just need to change precedence to switch between part 1 or 2
precedence = {
        "+":2,
        "-":2,
        "*":1,
        "/":1,
        "(":0,
        ")":0
        }



def eval(expr: str) -> int:
    i = 0
    numbers = list()
    operators = list()
    while i < len(expr):
        if expr[i] == " ":
            i += 1
            continue
        elif expr[i].isnumeric():
            nstr = expr[i]
            i += 1
            while i < len(expr) and expr[i].isnumeric():
                nstr = nstr + expr[i]
                i += 1
            numbers.append(int(nstr))
            continue
        elif expr[i] == "(":
            operators.append(expr[i])
        elif expr[i] == ")":
            while operators[-1] != "(":
                op = operators.pop()
                b = numbers.pop()
                a = numbers.pop()
                numbers.append(apply(op, a, b))
            operators.pop()
        elif expr[i] in precedence:
            curr_op = expr[i]
            while len(operators) > 0 and precedence[operators[-1]] >= precedence[curr_op]:
                op = operators.pop()
                b = numbers.pop()
                a = numbers.pop()
                numbers.append(apply(op, a, b))
            operators.append(curr_op)
        i += 1
    while len(operators) > 0:
        op = operators.pop()
        b = numbers.pop()
        a = numbers.pop()
        numbers.append(apply(op, a, b))
    return numbers.pop()

expressions = parse("data")
print(sum( eval(x) for x in expressions ))
