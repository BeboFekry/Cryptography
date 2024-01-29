# vigenere decryption
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ciphertext = input("cipher text: ").upper()
key = input("key: ").upper()
plantext = ''
for i in range(len(ciphertext)):
    char = ciphertext[i]
    index = alpha.find(char)
    keychar = key[i%len(key)]
    keyindex = alpha.find(keychar) 
    index = (index-keyindex)%26
    plantext +=alpha[index]
print(f"plan text: {plantext}")
