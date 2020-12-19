import re

def parse(filename: str) -> dict:
    with open(filename, "r") as f:
        data = f.read()
    rules = { x.split(":")[0]:x.split(":")[1].replace("\"", "").strip() for x in data.split("\n\n")[0].split("\n")}
    lines = [line for line in data.split("\n\n")[1].split("\n") if line != ""]
    return rules, lines

def mrule(rules: dict) -> str:
    flag = True
    frule = rules["0"]
    while flag:
        flag = False
        for i, x in enumerate(frule):
            if x.isnumeric():
                l = 1
                while i+l+1 <= len(frule) and frule[i:i+l+1].isnumeric():
                    l += 1
                index = frule[i:i+l]
                if "|" in rules[index]:
                    #frule = frule.replace(index, "(?:" + rules[index] + ")") BIG ERROR WAS HERE
                    frule = re.sub(f"\\b{index}\\b", "(?:" + rules[index] + ")", frule)
                else:
                    #frule = frule.replace(index, rules[index]) AND HERE TOO replace("4", ...) will replace modify 45 to ...5
                    frule = re.sub(f"\\b{index}\\b", rules[index], frule)
                flag = True
                break
    return frule.replace(" ", "")

rules, lines = parse("data")
rules["8"] = "42 | 42 8"
rules["11"] = "42 31 | 42 11 31"
for _ in range(3): # 3 recursions is the minimum
    rules["8"] = rules["8"].replace("8", "(?:" + rules["8"] + ")")
    rules["11"] = rules["11"].replace("11", "(?:" + rules["11"] + ")")
rules["8"] = rules["8"].replace(" 8", "")
rules["11"] = rules["11"].replace(" 11", "")
expr = mrule(rules)

count = 0
for l in lines:
    res = re.fullmatch(expr, l)
    if res:
        count += 1
print(count)

