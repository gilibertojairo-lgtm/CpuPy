#!/bin/bash

FILE="$1"
MODE="$2"

if [ "$MODE" == "--hex" ]; then
    echo "== HEX =="
    assembler "$FILE" --hex
    exit 0
fi

echo "== BIN =="
python3 assembler.py "$FILE" --bin > program.bin

echo "== RUN =="
python ejecutar.py program.bin
