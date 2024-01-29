# affine decryption
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ciphertext = input("cipher text: ").upper()
key = int(input("key: "))
key2 = int(input("key2: "))
plantext = ''
keyinverse=0
for i in range(1,26,2):
    if i==13:
        continue
    if key*i %26==1:
        keyinverse = i
        break
for i in range(len(ciphertext)):
    char = ciphertext[i]
    index = alpha.find(char)
    index = (index-key2)%26
    index = (index*keyinverse)%26
    plantext +=alpha[index]
print(f"plan text: {plantext}")
