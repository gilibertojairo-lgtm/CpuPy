⚡ CpuPy (cpu8bit)

🧠 Descripción

CpuPy es un proyecto en Python que permite ejecutar programas para una CPU de 8 bits a partir de archivos en formato binario (".bin") o hexadecimal (".hex").

Incluye un paquete ("cpu8bit") que implementa la CPU y un script ("ejecutar.py") que permite cargar y ejecutar programas fácilmente desde la terminal.

---

🎯 Características

- 🧮 Ejecución de programas en formato .bin y .hex
- ⚙️ Simulación de una CPU de 8 bits
- 🔍 Detección automática del formato de entrada
- 🐍 Implementado en Python

---

📦 Estructura del proyecto

.
├── cpu8bit-0.1.5-py3-none-any.whl  # Implementación de la CPU
├── ejecutar.py                     # Script para ejecutar programas
└── README.md

---

🚀 Instalación

Instala el paquete ".whl":

pip install cpu8bit-0.1.5-py3-none-any.whl

---

▶️ Uso

Ejecuta un programa pasando el archivo como argumento:

python ejecutar.py programa.bin

o

python ejecutar.py programa.hex

---

⚙️ Funcionamiento

El script "ejecutar.py":

1. Recibe un archivo como argumento
2. Detecta automáticamente el formato:
   - ".bin" → modo binario
   - ".hex" → modo hexadecimal
3. Carga el programa en la CPU:
   cpu.load_program(archivo, mode="bin" | "hex")
4. Ejecuta el programa:
   cpu.run()

---

🧠 Sobre la CPU

El módulo "cpu8bit" implementa una CPU básica de 8 bits capaz de interpretar instrucciones desde archivos externos.

Dependiendo de la implementación interna, puede incluir:

- registros
- memoria
- set de instrucciones

---

🧪 Estado del proyecto

🚧 En desarrollo

Este proyecto es experimental y puede:

- cambiar sin aviso
- contener errores
- expandirse con nuevas instrucciones o features

---

⚠️ Nota

Este repositorio incluye el paquete compilado (".whl").
El código fuente del módulo "cpu8bit" puede no estar incluido.

---

📜 Licencia

Por definir

👽 Extra

El assembler se usa con 
``
python3 assembler.py ~/ejemplo.asm --hex 
python3 assembler.py ~/ejemplo1.asm --bin
``