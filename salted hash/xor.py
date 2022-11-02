import base64
from pwn import xor
flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
print(xor(flag, ''.encode())) # oh, it says 'myXORke+y...'

data = base64.b64encode(b'0123456789')
print(data)
