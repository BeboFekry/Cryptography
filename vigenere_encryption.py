# vigenere encryption
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plantext = input("plan text: ").upper()
key = input("key: ").upper()
ciphertext = ''
for i in range(len(plantext)):
    char = plantext[i]
    index = alpha.find(char)
    keychar = key[i%len(key)]
    keyindex = alpha.find(keychar) 
    index = (index+keyindex)%26
    ciphertext +=alpha[index]
print(f"cipher text: {ciphertext}")
