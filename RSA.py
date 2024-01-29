# RSA

import random
from math import gcd
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generate_key(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = random.randint(1, phi_n)
    while gcd(e, phi_n) != 1:
        e = random.randint(1, phi_n)    
    public_key = (n, e)
    return public_key

def encrypt(message, public_key):
    n, e = public_key
    ciphertext =''
    for i in range(len(message)):
        char=message[i]
        index = alpha.find(char)
        ciphertext += alpha[(index**e)%n  %26]
    return ciphertext

p = 61
q = 53
public_key = generate_key(p, q)

# message = "Hello Bebo"
plaintext = input("Plaintext: ").upper()
ciphertext = encrypt(plaintext, public_key)
print("Encrypted message:", ciphertext)
