#!/bin/bash

# Step 1: Download the necessary files
wget https://artifacts.picoctf.net/c_titan/47/ciphertext -O ciphertext
wget https://artifacts.picoctf.net/c_titan/47/convert.py -O convert.py

# Step 2: Create the decoding script
cat << 'EOF' > decode.py
import sys

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

chars = ""
from fileinput import input
for line in input():
    chars += line

decrypted_message = ""
prev = 0
for char in chars:
    cur = lookup2.index(char)
    decrypted_char_index = (cur + prev) % 40
    decrypted_message += lookup1[decrypted_char_index]
    prev = decrypted_char_index 

print(decrypted_message)
EOF

# Step 3: Run the decoding script
python3 decode.py < ciphertext > decrypted.txt

# Step 4: Create the second extraction script
cat << 'EOF' > extract.py
chars = ""
from fileinput import input
for line in input():
    chars += line
b = 1

for i in range(len(chars)):
    if i == (b * b * b):
        print(chars[i], end="")
        b += 1

print()
EOF

# Step 5: Extract relevant characters
extracted=$(python3 extract.py < decrypted.txt)

# Step 6: Format the output
flag="picoCTF{${extracted}}"

# Step 7: Print the final flag
echo "Flag: $flag"
