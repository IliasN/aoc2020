class AdventProcessor:
    def __init__(self):
        self.__instructions = []
        self.__pc = 0
        self.__acc = 0

    @classmethod
    def with_instructions(cls, instructions):
        if type(instructions) != list:
            raise ValueError("Instructions must be list of str.")
        o = AdventProcessor()
        o.__instructions = instructions.copy()
        return o

    def __repr__(self):
        return f"AdventProcessor({len(self.__instructions)})"

    def __getitem__(self, key):
        return self.__instructions[key]

    def run(self, check_loop=False, debug=False, verbose=False):
        if check_loop:
            instr_set = set()
        self.__pc = 0
        self.__acc = 0
        while self.__pc < len(self.__instructions):
            if debug:
                print(self[self.__pc], "PC :", self.__pc, "ACC :", self.__acc)
            if check_loop:
                if self.__pc in instr_set:
                    if verbose:
                        self.__dump_loop_infos()
                    return 1
                else:
                    instr_set.add(self.__pc)
            self.__exec_instr()
        return 0

    def __exec_instr(self):
        instr = self[self.__pc]
        cmd,value = instr.split()
        if cmd == "nop":
            self.__pc += 1
        elif cmd == "acc":
            self.__acc += int(value)
            self.__pc += 1
        elif cmd == "jmp":
            self.__pc += int(value)
        else:
            stderr.write(f"Instruction {cmd} unknown")

    def acc(self):
        return self.__acc

    def pc(self):
        return self.__pc

    def __dump_loop_infos(self):
        print(f"Instruction {self[self.__pc]} at {self.__pc} already executed once")
        print(f"Acc : {self.__acc}")



with open("data", "r") as f:
    lines = [ line.replace("\n", "") for line in f if line != "\n" ]

print("Part 1 :")
my_proc = AdventProcessor.with_instructions(lines)
my_proc.run(True, False, True)

print("Part 2 :")
for i, instr in enumerate(lines):
    lines_c = lines.copy()
    if "nop" in instr:
        lines_c[i] = lines_c[i].replace("nop", "jmp")
    if "jmp" in instr:
        lines_c[i] = lines_c[i].replace("jmp", "nop")
    my_proc = AdventProcessor.with_instructions(lines_c)
    return_value = my_proc.run(True, False)
    if return_value == 0:
        print(f"Sucessful run finished !\nAcc : {my_proc.acc()}")
