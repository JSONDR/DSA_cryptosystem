import hashlib as hashy
import random

# (L, N) = (3072, 256)
# Mixed Key of Parameters: (H, output), (L, key_length), (N, modulus_length), (block_time, seconds), (block_size, megabytes)

#q is a N-bit prime
#p is a L-bit prime such that p - 1 = kq

def str_to_hash(_str):
    _hash = hashy.sha256(_str.encode('utf-8'))
    H_m = int.from_bytes(_hash.digest(), 'big')
    return H_m

#seed_phrase is a 16 word digest
#invoke to generate the keys of a wallet
def generate_keys(p, q, g, seed_phrase):
    H_m = str_to_hash(seed_phrase)

    #compute private key
    #note that x in (1, q - 1)
    x = H_m % q 

    if(x == 0):
        print("Try a different seed phrase")
        return (0, 0)
    
    #compute public key
    y = pow(g, x, p)
    return (x, y)

def setup_parameter_g(p, q):
    #setup
    h = 2
    exponent = (p - 1) // q
    g = pow(h, exponent, p)
    while(g == 0):
        print("Since g is zero, regenerate h, then recompute g")
        h = random.randint(2, p - 2)
        g = pow(h, exponent, p)
    return g