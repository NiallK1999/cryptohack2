# import the hashlib library for performing hashing functions
from codecs import utf_16_be_decode
import hashlib

# Create an initial test string
some_string = "Hello World!"

some_string.encode('utf-8') 



print(some_string)

# Create an MD5 hash object
hash = hashlib.md5()

# Update our hash object with the string
hash.update(some_string.encode('utf-8'))

# Print out our hash in hex format
print (hash.hexdigest())