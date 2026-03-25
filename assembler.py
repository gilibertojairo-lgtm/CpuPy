OPCODES = {
    "LOAD": 1,
    "ADD": 2,
    "CMP": 3,
    "PRINT": 4,
    "PRINTC": 5,
    "JMP": 6,
    "JZ": 7,
    "HALT": 255
}

REGISTERS = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3
}

def parse_value(v):
    # permite numeros o caracteres ASCII
    if v.startswith("'") and v.endswith("'"):
        return ord(v[1])
    return int(v)

def assemble_line(line):
    parts = line.strip().split()

    if not parts or parts[0].startswith("#"):
        return []

    instr = parts[0].upper()

    if instr not in OPCODES:
        raise ValueError(f"Instrucción desconocida: {instr}")

    opcode = OPCODES[instr]
    bytes_out = [opcode]

    if instr == "LOAD":
        reg = REGISTERS[parts[1].upper()]
        val = parse_value(parts[2])
        bytes_out.extend([reg, val])

    elif instr == "ADD":
        r1 = REGISTERS[parts[1].upper()]
        r2 = REGISTERS[parts[2].upper()]
        bytes_out.extend([r1, r2])

    elif instr == "CMP":
        r1 = REGISTERS[parts[1].upper()]
        r2 = REGISTERS[parts[2].upper()]
        bytes_out.extend([r1, r2])

    elif instr == "PRINT":
        reg = REGISTERS[parts[1].upper()]
        bytes_out.append(reg)

    elif instr == "PRINTC":
        val = parse_value(parts[1])
        bytes_out.append(val)

    elif instr == "JMP":
        addr = int(parts[1])
        bytes_out.append(addr)

    elif instr == "JZ":
        addr = int(parts[1])
        bytes_out.append(addr)

    elif instr == "HALT":
        pass

    return bytes_out


def format_byte(b, mode):
    if mode == "bin":
        return f"{b:08b}"
    elif mode == "hex":
        return f"{b:02X}"
    else:
        raise ValueError("Modo inválido")


def assemble_console(input_file, mode="bin"):
    with open(input_file, "r") as f:
        for line in f:
            bytes_line = assemble_line(line)
            for b in bytes_line:
                print(format_byte(b, mode))


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Uso: python assembler.py programa.asm [--bin | --hex]")
    else:
        mode = "bin"
        if len(sys.argv) > 2:
            if sys.argv[2] == "--hex":
                mode = "hex"
            elif sys.argv[2] == "--bin":
                mode = "bin"

        assemble_console(sys.argv[1], mode)