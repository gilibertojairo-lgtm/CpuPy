import os

class CPU8Bit:
    def __init__(self, num_regs=4, mem_size=256):
        self.R = [0] * num_regs
        self.memory = [0] * mem_size
        self.PC = 0
        self.running = False

    # ---- Funciones de seguridad para registros y memoria ----
    def get_reg(self, idx):
        if 0 <= idx < len(self.R):
            return self.R[idx]
        raise IndexError(f"Registro inválido: {idx}")

    def set_reg(self, idx, val):
        if 0 <= idx < len(self.R):
            self.R[idx] = val & 0xFF
        else:
            raise IndexError(f"Registro inválido: {idx}")

    def get_mem(self, addr):
        if 0 <= addr < len(self.memory):
            return self.memory[addr]
        raise IndexError(f"Dirección de memoria inválida: {addr}")

    def set_mem(self, addr, val):
        if 0 <= addr < len(self.memory):
            self.memory[addr] = val & 0xFF
        else:
            raise IndexError(f"Dirección de memoria inválida: {addr}")

    # ---- Cargar programa en binario o hex ----
    def load_program(self, filename, mode="bin"):
        """
        mode: "bin" = binario puro (default)
              "hex" = cada línea es un byte en hexadecimal (0x.. o sin 0x)
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"{filename} no encontrado")

        program = []
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if mode == "bin":
                    program.append(int(line, 2))
                elif mode == "hex":
                    line = line.lower().replace("0x", "")
                    for byte_str in line.split():  # permitir varios bytes por línea
                        program.append(int(byte_str, 16))
                else:
                    raise ValueError(f"Modo inválido: {mode}")

        if len(program) > len(self.memory):
            raise ValueError("Programa demasiado grande para la memoria")

        # limpiar memoria y copiar programa
        self.memory = [0] * len(self.memory)
        for i, b in enumerate(program):
            self.memory[i] = b

        self.PC = 0

    # ---- Ejecutar programa ----
    def run(self):
        self.PC = 0
        self.running = True

        while self.running:
            if self.PC >= len(self.memory):
                print("ERROR: PC fuera de memoria")
                break

            opcode = self.memory[self.PC]
            self.PC += 1

            try:
                if opcode == 0:
                    continue  # ignorar ceros basura

                elif opcode == 1:  # LOAD reg val
                    reg = self.memory[self.PC]; self.PC += 1
                    val = self.memory[self.PC]; self.PC += 1
                    self.set_reg(reg, val)

                elif opcode == 2:  # ADD regA regB
                    a = self.memory[self.PC]; self.PC += 1
                    b = self.memory[self.PC]; self.PC += 1
                    self.set_reg(a, self.get_reg(a) + self.get_reg(b))

                elif opcode == 3:  # SUB regA regB
                    a = self.memory[self.PC]; self.PC += 1
                    b = self.memory[self.PC]; self.PC += 1
                    self.set_reg(a, self.get_reg(a) - self.get_reg(b))

                elif opcode == 4:  # PRINT reg
                    reg = self.memory[self.PC]; self.PC += 1
                    val = self.get_reg(reg)
                    # imprimir carácter visible o número entre <>
                    if 32 <= val <= 126:
                        print(chr(val), end='')
                    else:
                        print(val, end='')  # solo imprime el número
                elif opcode == 5:  # PRINTSTR (bytes hasta 0)
                    while self.PC < len(self.memory):
                        val = self.memory[self.PC]; self.PC += 1
                        if val == 0:
                            break
                        if 32 <= val <= 126:
                            print(chr(val), end='')
                        else:
                            print(f"<{val}>", end='')

                elif opcode == 6:  # STORE reg addr
                    reg = self.memory[self.PC]; self.PC += 1
                    addr = self.memory[self.PC]; self.PC += 1
                    self.set_mem(addr, self.get_reg(reg))

                elif opcode == 7:  # LOADM reg addr
                    reg = self.memory[self.PC]; self.PC += 1
                    addr = self.memory[self.PC]; self.PC += 1
                    self.set_reg(reg, self.get_mem(addr))

                elif opcode == 8:  # JMP addr
                    addr = self.memory[self.PC]; self.PC = addr

                elif opcode == 9:  # JZ reg addr
                    reg = self.memory[self.PC]; self.PC += 1
                    addr = self.memory[self.PC]; self.PC += 1
                    if self.get_reg(reg) == 0:
                        self.PC = addr

                elif opcode == 255:  # HALT
                    self.running = False
                    print()
                else:
                    print(f"ERROR: opcode {opcode}")
                    self.running = False

            except IndexError as e:
                print(f"ERROR: {e}")
                self.running = False
