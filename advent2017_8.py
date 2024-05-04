registers = {}

largest = 0
with open("input2017_8.txt") as f:
    for line in f:
        line = line.strip().split()
        register1, instruction, amount, _, register2, compare, comparison = line
        amount = int(amount)
        comparison = int(comparison)
        print(register1, instruction, amount, register2, compare, comparison)
        if instruction == "dec":
            amount *= -1
        if register1 not in registers:
            registers[register1] = 0
        if register2 not in registers:
            registers[register2] = 0
        if compare == "==" and registers[register2] == comparison:
            registers[register1] += amount
        elif compare == ">" and registers[register2] > comparison:
            registers[register1] += amount
        elif compare == "<" and registers[register2] < comparison:
            registers[register1] += amount
        elif compare == ">=" and registers[register2] >= comparison:
            registers[register1] += amount
        elif compare == "<=" and registers[register2] <= comparison:
            registers[register1] += amount
        elif compare == "!=" and registers[register2] != comparison:
            registers[register1] += amount
        if registers[register1] > largest:
            largest = registers[register1]

print(max(registers.values()))
print(largest)