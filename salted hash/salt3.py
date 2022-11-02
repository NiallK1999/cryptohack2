import hashlib


hash = hashlib.md5()
hash.update(b"noob")
print(hash.hexdigest())
# seed is noob 

hash = hashlib.md5()
hash.update(b"noob")
print(hash.hexdigest())