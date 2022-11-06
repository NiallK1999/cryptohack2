
from quopri import encodestring
from pwn import * # pip install pwntools
import json
import codecs, base64 
from Crypto.Util.number import long_to_bytes 

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def decoded(encoded_string, encoded_type):
    if encoded_type == 'base64':
        return bytes(base64.b64decode(encoded_string)).decode("utf-8")

    elif encoded_type == 'hex':
        return bytes(bytes.fromhex(encoded_string, "rot13")).decode("utf-8")

    elif encoded_type == 'rot13':
        return codecs.decode(encoded_string)

    elif encoded_type == 'utf-8':
        return ''.join(chr(i) for i in encoded_string)

    else: encoded_type == 'bigint'
    return bytes(long_to_bytes(int(encoded_string, 16))).decode("utf-8")





#print("Received type: ", received["type"])

#print("Received encoded value: ", received["encoded"])





for i in range(100):
    received = json_recv()
    print("Received type: ", received["type"])
    encoded_type = received["type"]



    print("Received encoded value: ", received["encoded"])
    encode_string = received["encoded"]

    to_send = {
    "decoded": decoded(encodestring, encoded_type)
    }
    json_send(to_send)
