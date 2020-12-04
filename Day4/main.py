with open("data", "r") as f:
    lines = [line for line in f]

passeports = []
current_passport = dict()
for line in lines:
    if len(line) == 1:
        passeports.append(current_passport)
        current_passport = dict()
        continue
    line = line.replace("\n", "")
    datas = line.split(" ")
    for champ in datas:
        key = champ.split(":")[0]
        value = champ.split(":")[1]
        current_passport[key] = value
if current_passport and current_passport != passeports[-1]:
    passeports.append(current_passport)


count = 0
for p in passeports:
    if "byr" in p and "iyr" in p and "eyr" in p and "hgt" in p and "hcl" in p and "ecl" in p and "pid" in p:
        count += 1
print(count)
