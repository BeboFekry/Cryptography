# affine encryption
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plantext = input("plan text: ").upper()
key = int(input("key: "))    #for multiplication
key2 = int(input("key2: "))  #for addition
ciphertext = ''
for i in range(len(plantext)):
    char = plantext[i]
    index = alpha.find(char)
    index = (index*key)%26
    index = (index+key2)%26
    ciphertext +=alpha[index]
print(f"cipher text: {ciphertext}")
