import hashlib


seed = hashlib.md5()
seed.update(b"noob")

print("the seed of the USER ECSC is : " + seed.hexdigest() )


hash = hashlib.md5()
hash.update()
hash.hexdigest()
# hash = hashlib.md5()
hash_authenticate = hash.hexdigest()


while 1:
    hash = hashlib.md5(hash.hexdigest()) # create the the second hash
    if(hash.hexdigest() == "c89aa2ffb9edcc6604005196b5f0e0e4"):
        break # use break instead of continue to quit the loop instead of return to the begging of the loop
    hash_authenticate = hash.hexdigest() # save the old hash

print("FOUND : "  + hash_authenticate) # authenticate hash is the hash that give the challenge hash