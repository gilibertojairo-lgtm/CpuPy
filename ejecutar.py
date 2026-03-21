# ejecutar.py
import sys
from cpu import CPU8Bit
import os

if len(sys.argv) < 2:
    print("Uso: python3 ejecutar.py archivo.bin o archivo.hex")
    sys.exit(1)

archivo = sys.argv[1]

cpu = CPU8Bit()

# Detectar automáticamente el modo según la extensión
ext = os.path.splitext(archivo)[1].lower()
if ext == ".bin":
    mode = "bin"
elif ext == ".hex":
    mode = "hex"
else:
    print("Archivo desconocido, use .bin o .hex")
    sys.exit(1)

# Cargar el programa con el modo correcto
cpu.load_program(archivo, mode=mode)

# Ejecutar el programa
cpu.run()
