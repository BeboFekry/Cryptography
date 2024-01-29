# additive decryption
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ciphertext = input("cipher text: ").upper()
key = int(input("key: "))
plantext = ''
for i in range(len(ciphertext)):
    char = ciphertext[i]
    index = alpha.find(char)
    index = (index-key)%26
    plantext +=alpha[index]
print(f"plan text: {plantext}")
