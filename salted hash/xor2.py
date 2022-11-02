import base64
from pwn import xor
flag = bytes.base64('0f295b9e67f362f1be3cd7d0b30d4f4007f88a0e')
print(xor(flag, '0123456789'.encode())) # oh, it says 'myXORke+y...'

