def parse(filename: str) -> list:
    with open(filename, "r") as f:
        lines = [ line.replace("\n", "") for line in f if line != "\n" ]
    return lines


class Memory:
    def __init__(self, instructions):
        self.instructions = instructions.copy()
        self.mem_len = self.get_len()
        self.mem = [0] * (self.mem_len + 1)
        self.mask_set = 0
        self.mask_unset = 0

    def get_len(self) -> int:
        return max( int(x.split("[")[1].split("]")[0]) for x in self.instructions if "mem" in x)

    def run(self) -> None:
        for instr in self.instructions:
            if "mem" in instr:
                i = int(instr.split("[")[1].split("]")[0])
                val = int(instr.split("=")[1].strip())
                self.set_mem(i, val)
            elif "mask" in instr:
                s = instr.split("=")[1].strip()
                self.set_mask(s)
            else:
                print(f"Unknown command : {instr}")

    def set_mem(self, index: int, value: int) -> None:
        self.mem[index] = (value | self.mask_set) & self.mask_unset

    def set_mask(self, s: str) -> None:
        self.mask_set = int(s.replace("X", "0"), 2)
        self.mask_unset = int(s.replace("X", "1"), 2)

    def get_sum(self) -> int:
        return sum(self.mem)

class Memory2:
    def __init__(self, instructions):
        self.instructions = instructions.copy()
        #self.mem_len = self.get_len()
        #self.mem = [0] * self.mem_len
        self.mem = dict()
        self.mask = ""

    def get_len(self) -> int:
        return max( int(x.split("[")[1].split("]")[0]) for x in self.instructions if "mem" in x)

    def run(self) -> None:
        for instr in self.instructions:
            if "mem" in instr:
                i = int(instr.split("[")[1].split("]")[0])
                val = int(instr.split("=")[1].strip())
                self.set_mem(i, val)
            elif "mask" in instr:
                s = instr.split("=")[1].strip()
                self.set_mask(s)
            else:
                print(f"Unknown command : {instr}")

    def set_mem(self, index: int, value: int) -> None:
        addr_s = self.addr_from_mask(index)
        nb_s = len([ x for x in addr_s if x == "X" ])
        combis = list()
        self.bit_combi(combis, nb_s, 0, list())
        for co in combis:
            addr = self.addr_from_array(addr_s, co)
            #if addr >= len(self.mem):
                #self.resize_mem(addr)
            self.mem[addr] = value

    def resize_mem(self, addr: int) -> None:
        concat_arr = [0] * (addr - len(self.mem) + 1)
        self.mem = self.mem + concat_arr

    @staticmethod
    def addr_from_array(addr_s: str, arr: list) -> int:
        arr_i = 0
        new_str = ""
        for i, c in enumerate(addr_s):
            if c != "X":
                new_str = new_str + c
            else:
                new_str = new_str + str(arr[arr_i])
                arr_i += 1
        return int(new_str, 2)



    def set_mask(self, s: str):
        self.mask = s

    def get_sum(self):
        return sum(list(self.mem.values()))
    
    @staticmethod
    def bit_combi(arr: list, n: int, i: int, curr: list) -> None:
        if n == i:
            arr.append(curr)
        else:
            my_curr0 = curr.copy()
            my_curr0.append(0)
            Memory2.bit_combi(arr, n, i+1, my_curr0)
            my_curr1 = curr.copy()
            my_curr1.append(1)
            Memory2.bit_combi(arr, n, i+1, my_curr1)

    def addr_from_mask(self, addr: int) -> str:
        addr_s = bin(addr)[2:]
        while len(addr_s) < 36:
            addr_s = "0" + addr_s
        ret_addr = ""
        for i,c in enumerate(self.mask):
            if c == "1":
                ret_addr = ret_addr + "1"
            elif c == "X":
                ret_addr = ret_addr + "X"
            elif c == "0":
                ret_addr = ret_addr + addr_s[i]
            else:
                print("There is a problem here...")
        return ret_addr


data = parse("data")
mem = Memory(data)
mem.run()
res1 = mem.get_sum()
print("Part 1 :")
print(res1)

mem2 = Memory2(data)
mem2.run()
res2 = mem2.get_sum()
print("Part 2 :")
print(res2)
